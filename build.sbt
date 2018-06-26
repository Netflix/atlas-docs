
val generateSearchIndex = taskKey[(File, String)]("Generate search index of the site.")
val checkLinks = taskKey[Unit]("Check links in the generated pages.")

lazy val root = (project in file("."))
  .enablePlugins(ParadoxSitePlugin, GhpagesPlugin)
  .settings(
    name := "Atlas Docs",
    paradoxDirectives ++= Seq(
      GraphDirective,
      StacklangDirective,
      ExampleDirective
    ),
    paradoxTheme := None,
    paradoxNavigationDepth := 3,
    paradoxGroups := Map("Language" -> Seq("Java", "Python")),
    sourceDirectory in Paradox := sourceDirectory.value / "main" / "paradox",
    sourceDirectory in Paradox in paradoxTheme := sourceDirectory.value / "main" / "paradox" / "_template",
    previewFixedPort := Some(8000), // Match mkdocs default
    previewLaunchBrowser := false,

    generateSearchIndex := Def.taskDyn {
      // Ensure html has been generated
      val mappings = (paradoxMarkdownToHtml in Paradox).value
      val dir = (target in Paradox).value / "paradox" / "site" / "paradox"

      // Generate the index
      val indexFile = dir / "search.json"
      SearchIndex.generate(indexFile, mappings)
      Def.task((indexFile, "search.json"))
    }.value,

    mappings in Paradox += generateSearchIndex.value,

    checkLinks := Def.taskDyn {
      // Ensure html has been generated
      val mappings = (paradoxMarkdownToHtml in Paradox).value
      val dir = (target in Paradox).value / "paradox" / "site" / "paradox"

      // Check the links
      val checker = new LinkChecker(streams.value.log)
      checker.check(mappings)
      Def.task(())
    }.value,

    git.remoteRepo := "git@github.com:Netflix/atlas-docs.git",

    libraryDependencies ++= Seq(
      "com.netflix.spectator" % "spectator-api" % "0.63.0",
      "javax.inject" % "javax.inject" % "1"
    )
  )
