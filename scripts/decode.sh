#!/bin/bash
rm -f "$2"*
base64 -d "$1" > "$2"
rm -f "$1"
