#!/bin/sh

cd "`dirname $0`"

python setup.py --long-description | rst2html > output.html && chromium-browser output.html

cd -
