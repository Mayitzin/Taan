# -*- coding: utf-8 -*-
"""
Tesseract OCR fraktur

@author: Mario Garcia
www.mayitzin.com
"""

import sys
import subprocess

input = "page001.png"
output = "page001"

# Read extra parameters
if len(sys.argv) >= 2:
    input = sys.argv[1]
    output = input[:-4]

subprocess.call(["tesseract", input, output, "-l deu-frak"])