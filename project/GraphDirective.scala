
import java.net.URI
import java.util.Base64

import akka.http.scaladsl.model.Uri
import com.lightbend.paradox.markdown.ContainerBlockDirective
import com.lightbend.paradox.markdown.Directive
import com.lightbend.paradox.markdown.Writer
import com.netflix.atlas.config.ConfigManager
import com.netflix.atlas.core.db.StaticDatabase
import com.netflix.atlas.core.util.PngImage
import com.netflix.atlas.core.util.Strings
import com.netflix.atlas.eval.graph.Grapher
import com.typesafe.config.ConfigFactory
import org.pegdown.Printer
import org.pegdown.ast.DirectiveNode
import org.pegdown.ast.Visitor

case class GraphDirective(context: Writer.Context)
  extends ContainerBlockDirective("atlas-graph") {

  private val config = ConfigFactory.load(getClass.getClassLoader)
  ConfigManager.set(config)

  private val db = new StaticDatabase(config.getConfig("atlas.core.db"))
  private val grapher = Grapher(config)

  private val basePath = "../" * context.location.depth


  def render(node: DirectiveNode, visitor: Visitor, printer: Printer): Unit = {
    val uri = Uri(node.contents.trim)
    val image = grapher.evalAndRender(uri, db)
    val meta = PngImage(image.data)
    val width = meta.data.getWidth
    val height = meta.data.getHeight

    val encoded = Base64.getEncoder.encodeToString(image.data)
    val dataUri = s"data:image/png;base64,$encoded"

    if (node.attributes.booleanValue("show-expr", false)) {
      printer.print(s"""<div>${formatQuery(uri.toString())}</div>""")
    }
    printer.print(s"""<div><image src="$dataUri" alt="$uri" width="$width" height="$height"/></div>""")
  }

  def formatQuery(line: String): String = {
    val uri = URI.create(line)
    val params = Strings.parseQueryString(uri.getQuery)
    val pstr = params.toList.sortWith(_._1 < _._1).flatMap {
      case (k, vs) =>
        vs.map { v =>
          if (k == "q") formatQueryExpr(v) else s"$k=$v"
        }
    }
    s"<pre>\n${uri.getPath}?\n  ${pstr.mkString("\n  &")}\n</pre>\n"
  }

  private def mkLink(prg: List[Any], name: String): String = {
    s"""<a href="${basePath}asl-reference/$name.html">:$name</a>"""
  }

  private def formatQueryExpr(q: String): String = {
    val parts = q.split(",").toList
    val buf = new StringBuilder
    buf.append("q=\n    ")
    parts.zipWithIndex.foreach {
      case (p, i) =>
        if (p.startsWith(":"))
          buf.append(mkLink(parts.take(i), p.substring(1))).append(',').append("\n    ")
        else
          buf.append(p).append(',')
    }
    val s = buf.toString
    s.substring(0, s.lastIndexOf(","))
  }
}

