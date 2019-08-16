# -*- coding: utf-8 -*-
"""
Tesseract OCR fraktur test

@author: Mario Garcia
www.mariogc.com
"""

import sys
import pytesseract

fileName = "page001.png"
output = "page001"

truth_file = "truth_page001.txt"
with open(truth_file, "r", encoding="utf-8") as f:
    truth_lines = f.readlines()

text = pytesseract.image_to_string(fileName, lang="deu_frak")
ocr_lines = text.split('\n')

num_words = 0
num_wrong_words = 0
if len(truth_lines) == len(ocr_lines):
    for idx, (tline, oline) in enumerate(zip(truth_lines, ocr_lines)):
        twords = tline.split()
        owords = oline.split()
        wrong_words = [i for i, j in zip(owords, twords) if i != j]
        num_words += len(twords)
        num_wrong_words += len(wrong_words)
print("Accuracy: {:.4f} %".format(100.0*(1.0-(num_wrong_words/num_words))))
