
import java.util.Base64

import akka.http.scaladsl.model.Uri
import com.lightbend.paradox.markdown.ContainerBlockDirective
import com.lightbend.paradox.markdown.Directive
import com.lightbend.paradox.markdown.Writer
import com.netflix.atlas.config.ConfigManager
import com.netflix.atlas.core.db.StaticDatabase
import com.netflix.atlas.core.util.PngImage
import com.netflix.atlas.eval.graph.Grapher
import com.typesafe.config.ConfigFactory
import org.pegdown.Printer
import org.pegdown.ast.DirectiveNode
import org.pegdown.ast.Visitor

case class ExampleDirective(context: Writer.Context)
  extends ContainerBlockDirective("atlas-example") {

  private val config = ConfigFactory.load(getClass.getClassLoader)
  ConfigManager.set(config)

  private val db = new StaticDatabase(config.getConfig("atlas.core.db"))
  private val grapher = Grapher(config)

  private val basePath = "../" * (context.location.depth - 1)

  private def parseLine(line: String): (String, String) = {
    val sep = line.indexOf(':')
    if (sep == -1)
      "-" -> line
    else
      line.substring(0, sep).trim -> line.substring(sep + 1).trim
  }

  def render(node: DirectiveNode, visitor: Visitor, printer: Printer): Unit = {
    val columns = node.contents.trim
      .split("\n")
      .map(_.trim)
      .filterNot(_.isEmpty)
      .map(parseLine)
      .toList

    val n = columns.size
    val contentWidth = 700 // with current style sheet the table with is 704
    val imageWidth = contentWidth / n
    val imageHeight = math.max(imageWidth / 2, 100)
    val params = s"&layout=image&w=$imageWidth&h=$imageHeight"

    val images = columns.map { c =>
      val uri = Uri(c._2 + params)
      val image = grapher.evalAndRender(uri, db)
      // Show the user the input uri without the additional rendering restrictions
      // injected for the docs
      ExampleDirective.createImageInfo(Uri(c._2), image)
    }

    printer.print(s"""
      <table>
        <thead>
          <tr>
            ${columns.map(c => s"<th>${c._1}</th>").mkString}
          </tr>
        </thead>
        <tbody>
          <tr>
            ${images.map(i => s"<td>${i.exprHtml(basePath)}</td>").mkString}
          </tr><tr>
            ${images.map(i => s"<td>${i.imageHtml}</td>").mkString}
          </tr>
        </tbody>
      </table>
    """)
  }
}

object ExampleDirective extends (Writer.Context => Directive) {

  def apply(context: Writer.Context): Directive = new ExampleDirective(context)

  def createImageInfo(uri: Uri, image: Grapher.Result): ImageInfo = {
    val meta = PngImage(image.data)
    val width = meta.data.getWidth
    val height = meta.data.getHeight
    val encoded = Base64.getEncoder.encodeToString(image.data)
    val dataUri = s"data:image/png;base64,$encoded"

    ImageInfo(uri, dataUri, width, height)
  }

  case class ImageInfo(uri: Uri, dataUri: String, width: Int, height: Int) {

    def exprHtml(basePath: String): String = {
      StacklangDirective.formatExpr(basePath, uri.query().getOrElse("q", ""))
    }

    def imageHtml: String = {
      s"""<image src="$dataUri" alt="$uri" width="$width" height="$height"/>"""
    }
  }
}

