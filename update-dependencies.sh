#!/usr/bin/env bash

echo "-- remove current venv"
rm -rf venv

echo "-- remove current requirements.txt"
rm requirements.txt

echo "-- remove cached atlas-standalone.jar"
rm -f atlas-standalone.jar

echo "-- create new venv with no deps"
./setup-venv.sh

echo "-- activate venv"
source venv/bin/activate


DEPS=( \
  mkdocs-material \
  mkdocs-markdownextradata-plugin \
  mkdocs-minify-plugin \
  plugins/atlas-link-checker \
  plugins/mkdocs-atlas-formatting-plugin \
)

echo "-- add dep tools to venv"
pip3 install --upgrade pip wheel

echo "-- install deps"
pip3 install --upgrade ${DEPS[@]}

echo "-- create requirements.txt"
pip3 freeze |egrep -v "atlas-link-checker|mkdocs-atlas-formatting-plugin" > requirements.txt
echo "-e plugins/atlas-link-checker" >> requirements.txt
echo "-e plugins/mkdocs-atlas-formatting-plugin" >> requirements.txt

echo "-- deactivate venv"
deactivate

