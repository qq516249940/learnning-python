#!/usr/bin/env python
import os

if os.path.isdir("/tmp"):
  print "/tmp is a dir"
else:
  print "/tmp is not a dir"
