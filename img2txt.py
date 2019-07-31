# -*- coding: utf-8 -*-
"""
Tesseract OCR fraktur

@author: Mario Garcia
www.mayitzin.com
"""

import sys
import pytesseract

fileName = "page001.png"
# fileName = "outfile.png"
output = "page001"

truth_file = "truth_page001.txt"
with open(truth_file, "r", encoding="utf-8") as f:
    truth_lines = f.readlines()

text = pytesseract.image_to_string(fileName, lang="deu_frak")
ocr_lines = text.split('\n')

if len(truth_lines) == len(ocr_lines):
    for idx, (tline, oline) in enumerate(zip(truth_lines, ocr_lines)):
        tline = tline.replace(',', '')
        tline = tline.replace('.', '')
        twords = tline.split()
        # print(twords)
        oline = oline.replace(',', '')
        oline = oline.replace('.', '')
        owords = oline.split()
        # print(owords)
        wrong_words = [i for i, j in zip(twords, owords) if i != j]
        if wrong_words:
            print("Line {} has {} wrong words: {}".format(idx, len(wrong_words), " ".join(wrong_words)))
