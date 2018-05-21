
import java.net.URI
import java.util.regex.Pattern

import com.lightbend.paradox.markdown.ContainerBlockDirective
import com.lightbend.paradox.markdown.Directive
import com.lightbend.paradox.markdown.Writer
import com.netflix.atlas.core.util.Strings
import org.pegdown.Printer
import org.pegdown.ast.DirectiveNode
import org.pegdown.ast.Visitor

case class StacklangDirective(context: Writer.Context)
  extends ContainerBlockDirective("atlas-expr") {

  private val basePath = "../" * context.location.depth

  def render(node: DirectiveNode, visitor: Visitor, printer: Printer): Unit = {
    val formatted = StacklangDirective.addReferenceLinks(basePath, node.contents.trim)
    printer.print(formatted)
  }
}

object StacklangDirective extends (Writer.Context => Directive) {

  def apply(context: Writer.Context): Directive = new StacklangDirective(context)

  /** Format an existing Atlas graph URI. */
  def formatUri(basePath: String, uriStr: String): String = {
    val uri = URI.create(uriStr)
    val params = Strings.parseQueryString(uri.getQuery)
    val pstr = params.toList.sortWith(_._1 < _._1).flatMap {
      case (k, vs) =>
        vs.map { v =>
          if (k == "q") formatQueryExpr(basePath, v) else s"$k=$v"
        }
    }
    s"<pre>\n${uri.getPath}?\n  ${pstr.mkString("\n  &")}\n</pre>\n"
  }

  private def mkLink(basePath: String, name: String): String = {
    s"""<a href="${basePath}asl-reference/$name.html">:$name</a>"""
  }

  private def formatQueryExpr(basePath: String, q: String): String = {
    val parts = q.split(",").toList
    val buf = new StringBuilder
    buf.append("q=\n    ")
    parts.zipWithIndex.foreach {
      case (p, i) =>
        if (p.startsWith(":"))
          buf.append(mkLink(basePath, p.substring(1))).append(',').append("\n    ")
        else
          buf.append(p).append(',')
    }
    val s = buf.toString
    s.substring(0, s.lastIndexOf(","))
  }

  /**
    * Simply add links back to the reference docs for an expr. This allows the user to
    * hand format the expression however they like.
    */
  def addReferenceLinks(basePath: String, input: String): String = {
    val matcher = Pattern.compile(":([^,\\s]+)").matcher(input)
    val builder = new StringBuffer()
    while (matcher.find()) {
      val name = matcher.group(1)
      val link = mkLink(basePath, name)
      matcher.appendReplacement(builder, link)
    }
    matcher.appendTail(builder)
    "<pre>\n" + builder.toString + "\n</pre>\n"
  }
}
