
lazy val root = (project in file("."))
  .enablePlugins(ParadoxSitePlugin, GhpagesPlugin)
  .settings(
    name := "Atlas Docs",
    paradoxDirectives ++= Seq(
      GraphDirective,
      StacklangDirective
    ),
    paradoxTheme := None,
    paradoxNavigationDepth := 3,
    paradoxGroups := Map("Language" -> Seq("Java", "Python")),
    sourceDirectory in Paradox := sourceDirectory.value / "main" / "paradox",
    sourceDirectory in Paradox in paradoxTheme := sourceDirectory.value / "main" / "paradox" / "_template",
    previewFixedPort := Some(8000), // Match mkdocs default
    previewLaunchBrowser := false,

    makeSite := {
      val siteDir = makeSite.value
      SearchIndex.generate(siteDir)
      siteDir
    },

    git.remoteRepo := "git@github.com:Netflix/atlas-docs.git",

    libraryDependencies ++= Seq(
      "com.netflix.spectator" % "spectator-api" % "0.63.0",
      "javax.inject" % "javax.inject" % "1"
    )
  )
