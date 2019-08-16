# -*- coding: utf-8 -*-
"""
PDF to Text test

@author: Mario Garcia
www.mariogc.com
"""

import pytesseract

from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('Tinosos_-_Fernandez_de_Lizardi.pdf')
new_file = "tinosos_01.png"
images[0].save(new_file)

text = pytesseract.image_to_string(new_file, lang="spa_old")
print(text)
