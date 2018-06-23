import java.io.File
import java.io.IOException
import java.nio.charset.StandardCharsets

import com.netflix.atlas.core.util.Streams._
import com.netflix.atlas.json.Json
import org.jsoup.Jsoup
import org.jsoup.nodes.Element

object SearchIndex {

  def generate(indexFile: File, mappings: Seq[(File, String)]): Unit = {
    val docs = Docs(mappings.flatMap(m => extractSections(m._1, m._2)).toList)
    scope(fileOut(indexFile)) { out =>
      out.write(Json.encode(docs).getBytes(StandardCharsets.UTF_8))
    }
  }

  private def extractSections(file: File, href: String): List[Doc] = {
    import scala.collection.JavaConverters._

    val html = Jsoup.parse(file, "UTF-8")
    val elements = html.select("#content")
      .asScala
      .flatMap(_.children().asScala)

    val docs = List.newBuilder[Doc]
    val builder = new StringBuilder
    var doc: Doc = null
    var pageTitle: String = null
    elements.foreach { element =>
      if (isHeader(element)) {
        if (doc != null) {
          docs += doc.copy(text = builder.toString().trim)
          builder.delete(0, builder.length)
        }
        val location = href + element.select("a").attr("href")
        val title = element.text().trim
        if (doc == null) {
          // First header on the page
          pageTitle = title
        }
        doc = Doc(location, title, pageTitle)
      } else {
        builder.append(element.text()).append(' ')
      }
    }
    docs.result()
  }

  private def isHeader(element: Element): Boolean = {
    val name = element.tagName()
    name.length == 2 && name.charAt(0) == 'h'
  }

  // Use the same structure as mkdocs index
  case class Docs(docs: List[Doc])
  case class Doc(location: String, title: String, pageTitle: String, text: String = "")
}
