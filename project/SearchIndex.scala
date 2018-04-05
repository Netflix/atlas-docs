import java.io.File
import java.nio.charset.StandardCharsets

import com.netflix.atlas.core.util.Streams._
import com.netflix.atlas.json.Json
import org.jsoup.Jsoup
import org.jsoup.nodes.Element

object SearchIndex {

  def generate(dir: File): Unit = {
    val pages = listPages(dir)
    val docs = Docs(pages.flatMap(p => extractSections(dir, p)))
    val index = new File(dir, "search.json")

    scope(fileOut(index)) { out =>
      out.write(Json.encode(docs).getBytes(StandardCharsets.UTF_8))
    }
  }

  private def listPages(dir: File): List[File] = {
    dir.listFiles()
      .flatMap {
        case f if f.isFile && f.getName.endsWith(".html") => List(f)
        case f if f.isDirectory                           => listPages(f)
        case _                                            => Nil
      }
      .toList
  }

  private def extractSections(baseDir: File, file: File): List[Doc] = {
    import scala.collection.JavaConverters._

    val urlPath = path(baseDir, file)

    val html = Jsoup.parse(file, "UTF-8")
    val elements = html.select("#content")
      .asScala
      .flatMap(_.children().asScala)

    val docs = List.newBuilder[Doc]
    val builder = new StringBuilder
    var doc: Doc = null
    elements.foreach { element =>
      if (isHeader(element)) {
        if (doc != null) {
          docs += doc.copy(text = builder.toString().trim)
          builder.delete(0, builder.length)
        }
        val location = urlPath + element.select("a").attr("href")
        val title = element.text().trim
        doc = Doc(location, title)
      } else {
        builder.append(element.text()).append(' ')
      }
    }
    docs.result()
  }

  private def path(baseDir: File, file: File): String = {
    "/" + baseDir.toURI.relativize(file.toURI).getPath
  }

  private def isHeader(element: Element): Boolean = {
    val name = element.tagName()
    name.length == 2 && name.charAt(0) == 'h'
  }

  // Use the same structure as mkdocs index
  case class Docs(docs: List[Doc])
  case class Doc(location: String, title: String, text: String = "")
}
