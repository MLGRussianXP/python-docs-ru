#!/bin/bash

cd ..
mkdir -p .tx
touch .tx/config

cd ..
sed cpython/Doc/locales/.tx/config -e "s|file_filter            = ./<lang>/LC_MESSAGES/|trans.ru               = |; s|= pot/|= ../cpython/Doc/locales/pot/|;" > python-docs-ru/.tx/config
