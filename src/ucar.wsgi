#! /opt/rh/httpd24/root/var/www/ucar/html/env2/bin/python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/opt/rh/httpd24/root/var/www/ucar/html/env2/src')
from index import app as application
application.secret_key = '12345'
