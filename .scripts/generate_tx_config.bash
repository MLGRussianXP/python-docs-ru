#!/bin/bash

# run from the .scripts directory

cd ..
mkdir -p .tx
touch .tx/config

cd ..
sed cpython/Doc/locales/.tx/config -e "s|file_filter            = ./<lang>/LC_MESSAGES/|trans.ru               = |; s|= pot/|= ../cpython/Doc/locales/pot/|;" > python-docs-ru/.tx/config
sed -i -e "/trans.ru/ s/trans.ru\(.*\)/&\nfile_filter\1/; s/\(file_filter\)    /\1 /" python-docs-ru/.tx/config
