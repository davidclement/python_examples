#!/usr/bin/python

#-----------------------------------------------------
# get timestamp (mtime) of file and turn into datetime
#-----------------------------------------------------
import datetime
from os import stat
ts = (stat(path))[8]
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')