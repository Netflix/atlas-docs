
import com.lightbend.paradox.markdown.ContainerBlockDirective
import com.lightbend.paradox.markdown.Directive
import com.lightbend.paradox.markdown.Writer
import org.pegdown.Printer
import org.pegdown.ast.DirectiveNode
import org.pegdown.ast.Visitor

object StacklangDirective extends ContainerBlockDirective("asl") with (Writer.Context => Directive) {
  def apply(context: Writer.Context): Directive = StacklangDirective

  def render(node: DirectiveNode, visitor: Visitor, printer: Printer): Unit = {
    val classes = node.attributes.classesString
    printer.print(s"""<pre class="$classes">""")
    printer.print(node.contents.split(",").mkString(",\n").trim)
    printer.print("""</pre>""")
  }
}
