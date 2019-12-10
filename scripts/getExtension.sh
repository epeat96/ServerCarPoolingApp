#!/bin/bash
file "$1"  | awk '{ print $2 }' | awk '{ print tolower($0) }'
