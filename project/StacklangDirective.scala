
import java.net.URI
import java.util.regex.Matcher
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

  private val basePath = "../" * (context.location.depth - 1)

  def render(node: DirectiveNode, visitor: Visitor, printer: Printer): Unit = {
    val formatted = StacklangDirective.addReferenceLinks(basePath, node.contents.trim)
    printer.print(formatted)
  }
}

object StacklangDirective extends (Writer.Context => Directive) {

  private val preClasses = "class=\"prettyprint prettyprinted\""

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
    addReferenceLinks(basePath, s"${uri.getPath}?\n  ${pstr.mkString(s"\n  &")}")
  }

  /** Format an existing Atlas expression. */
  def formatExpr(basePath: String, exprStr: String): String = {
    val parts = exprStr.split(",").toList
    val buf = new StringBuilder
    parts.zipWithIndex.foreach {
      case (p, i) =>
        if (p.startsWith(":"))
          buf.append(p).append(",\n")
        else
          buf.append(p).append(',')
    }
    val s = buf.toString
    val formatted = s.substring(0, s.lastIndexOf(","))
    addReferenceLinks(basePath, formatted)
  }

  private def mkLink(basePath: String, name: String): String = {
    s"""<a href="${basePath}asl-reference/$name.html">:$name</a>"""
  }

  private def span(cls: String, value: String): String = {
    s"""<span class="$cls">$value</span>"""
  }

  private def keyword(v: String): String = span("kwd", v)

  private def punctuation(v: String): String = span("pun", v)

  private def comment(v: String): String = span("com", v)

  private def formatQueryExpr(basePath: String, q: String): String = {
    val parts = q.split(",").toList
    val buf = new StringBuilder
    buf.append("q=\n    ")
    parts.zipWithIndex.foreach {
      case (p, i) =>
        if (p.startsWith(":") || p.startsWith("--"))
          buf.append(p).append(",\n    ")
        else
          buf.append(p).append(",")
    }
    val s = buf.toString
    s.substring(0, s.lastIndexOf(","))
  }

  private def rewrite(matcher: Matcher, f: String => String): String = {
    val builder = new StringBuffer()
    while (matcher.find()) {
      val r = f(matcher.group(1))
      matcher.appendReplacement(builder, r)
    }
    matcher.appendTail(builder).toString
  }

  /**
    * Simply add links back to the reference docs for an expr. This allows the user to
    * hand format the expression however they like.
    */
  def addReferenceLinks(basePath: String, input: String): String = {
    import Pattern.compile
    val rewrites = List(
      // Need to exclude times like 9:00, but cover operations like :2over and :-rot
      compile(":([-2a-z][a-z][^,\\s]*)") -> ((n: String) => keyword(mkLink(basePath, n))),
      compile("(--[^,\\n]+)")            -> comment _,
      compile("(,)")                     -> punctuation _
    )

    val str = rewrites.foldLeft(input) { (acc, rw) =>
      val matcher = rw._1.matcher(acc)
      rewrite(matcher, rw._2)
    }

    s"<pre $preClasses><code>$str</code></pre>\n"
  }
}
