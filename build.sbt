lazy val root = (project in file("."))
  //.enablePlugins(ParadoxSitePlugin, ParadoxMaterialThemePlugin)
  .enablePlugins(ParadoxSitePlugin, GhpagesPlugin)
  .settings(
    name := "Atlas Docs",
    paradoxDirectives ++= Seq(
      GraphDirective,
      StacklangDirective
    ),
    /*ParadoxMaterialThemePlugin.paradoxMaterialThemeSettings(Paradox),
    paradoxMaterialTheme in Paradox ~= {
      _.withFavicon("images/atlas_logo_small.png")
        .withLogo("images/atlas_logo_small.png")
        .withRepository(uri("https://github.com/brharrington/atlas-docs"))
    },*/
    paradoxGroups := Map("Language" -> Seq("Java", "Python")),
    sourceDirectory in Paradox := sourceDirectory.value / "main" / "paradox",
    previewFixedPort := Some(8000), // Match mkdocs default
    previewLaunchBrowser := false,

    git.remoteRepo := "git@github.com:Netflix/atlas-docs.git",

    libraryDependencies ++= Seq(
      "com.netflix.spectator" % "spectator-api" % "0.63.0",
      "javax.inject" % "javax.inject" % "1"
    )
  )
