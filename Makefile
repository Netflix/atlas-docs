# Map stdin to /dev/null to avoid interactive prompts if there is some failure related to the
# build script.
SBT := cat /dev/null | project/sbt

.PHONY: build release

build:
	echo "Starting build"
	$(SBT) clean compile packageSite

release:
	echo "Starting release build"
	$(SBT) clean compile ghpagesPushSite

