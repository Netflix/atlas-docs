import java.io.File
import java.net.URI
import java.net.URL

import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import sbt.internal.util.MessageOnlyException
import sbt.util.Logger

import scala.util.Failure
import scala.util.Success
import scala.util.Try

class LinkChecker(logger: Logger) {

  private val baseUri = URI.create("http://localhost:8000/site")

  private val red = "\u001B[31m"
  private val reset = "\u001B[0m"

  def check(mappings: Seq[(File, String)]): Unit = {

    // Extract links from all the local pages
    val localLinks = mappings.map(m => m._2 -> Try(extractLinks(m._1))).toMap

    // Extract links from the remote pages or flag them as broken. This is needed
    // to verify anchors within the remote page.
    val remoteHrefs = localLinks.values
      .collect {
        case Success(links) => links
      }
      .flatMap { links =>
        links.hrefs.filter(isRemote).map(removeFragment)
      }
      .toSet
    val remoteLinks = remoteHrefs
      .map { href =>
        val url = URI.create(href).toURL
        href -> Try(extractLinks(url))
      }
      .toMap

    val siteLinks = localLinks ++ remoteLinks

    val badLinks = localLinks.foldLeft(0) { (acc, m) =>
      m match {
        case (loc, Success(page)) => acc + check(loc, page, siteLinks)
        case (_, Failure(t))      => acc
      }
    }
    if (badLinks > 0)
      throw new MessageOnlyException(s"Found $badLinks broken links")
    else
      logger.info("All links work")
  }

  private def check(loc: String, page: Links, siteLinks: Map[String, Try[Links]]): Int = {
    logger.info(s"Checking $loc...")
    val badHrefs = page.hrefs.foldLeft(0) { (acc, href) =>
      val (url, fragment) = resolve(loc, href)
      siteLinks.get(url) match {
        case Some(Success(links)) =>
          // Page exists, now we need to verify the fragment points to a valid location
          // in the page
          if (fragment.forall(links.anchors.contains)) {
            acc
          } else {
            logger.error(s"- SECTION NOT FOUND: $href")
            acc + 1
          }
        case Some(Failure(t)) =>
          logger.error(s"- BAD PAGE: $href (${t.getClass.getName}: ${t.getMessage})")
          acc + 1
        case None =>
          logger.error(s"- NOT FOUND: $href (resolved: $url)")
          acc + 1
      }
    }
    val badImages = 0
    badHrefs + badImages
  }

  private def resolve(loc: String, href: String): (String, Option[String]) = {
    val fqUri = URI.create(s"$baseUri/$loc")
    val resolved = baseUri.relativize(fqUri.resolve(href)).toString
    val pos = resolved.indexOf('#')
    if (pos > 0)
      resolved.substring(0, pos) -> Some(resolved.substring(pos + 1)).filterNot(_.isEmpty)
    else
      resolved.toString -> None
  }

  private def extractLinks(file: File): Links = {
    logger.info(s"Processing $file...")
    val html = Jsoup.parse(file, "UTF-8")
    extractLinks(html)
  }

  private def extractLinks(url: URL): Links = {
    logger.info(s"Processing $url...")
    val html = Jsoup.parse(url, 30000)
    extractLinks(html)
  }

  private def extractLinks(html: Document): Links = {
    import scala.collection.JavaConverters._

    val anchors = html.select("a")
      .asScala
      .map(_.attr("name"))
      .filterNot(_.isEmpty)
      .toSet

    val hrefs = html.select("a")
      .asScala
      .map(_.attr("href"))
      .filterNot(_.isEmpty)
      .toList

    val images = html.select("img")
      .asScala
      .map(_.attr("src"))
      .filterNot(_.startsWith("data:"))
      .toList

    Links(anchors, hrefs, images)
  }

  private def isRemote(url: String): Boolean = {
    url.startsWith("http://") || url.startsWith("https://")
  }

  private def removeFragment(url: String): String = {
    val pos = url.indexOf('#')
    if (pos > 0) url.substring(0, pos) else url
  }

  case class Links(anchors: Set[String], hrefs: List[String], images: List[String])
}
