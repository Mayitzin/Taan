# -*- coding: utf-8 -*-
"""
Tesseract OCR fraktur

@author: Mario Garcia
www.mayitzin.com
"""

import sys
import subprocess

fileName = "page001.png"
output = "page001"

# Read extra parameters
if len(sys.argv) >= 2:
    fileName = sys.argv[1]
    output = fileName[:-4]

subprocess.call(["tesseract", fileName, output, "-l", "deu-frak"])