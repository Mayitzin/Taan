# -*- coding: utf-8 -*-
"""
Find text within an image

@author: Mario Garcia
www.mayitzin.com
"""

# Import required libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.ndimage as scimg
import numpy as np

# Load image
page = scimg.imread('page001.png')

# Show image
plt.imshow(page)
plt.show()