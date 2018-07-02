#! /bin/env python

import sys
from pbcpy.formats.qepp import PP
from pbcpy.formats.xsf import XSF

prefix = sys.argv[1]

system = PP(filepp=prefix+".pp").read()

XSF(filexsf=prefix+".xsf").write(system)


