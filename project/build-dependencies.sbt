
externalResolvers ++= Seq(
  //Resolver.mavenLocal,
  Resolver.jcenterRepo,
  "jfrog" at "http://oss.jfrog.org/oss-snapshot-local"
)

libraryDependencies ++= Seq(
  "com.netflix.atlas_v1" %% "atlas-eval" % "1.6.0-SNAPSHOT"
)
