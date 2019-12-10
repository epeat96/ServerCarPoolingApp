#!/bin/bash
EXTENSION=$(/opt/rh/httpd24/root/var/www/ucar/html/env2/scripts/getExtension.sh $1)
mv "$1" "$1""."$EXTENSION
