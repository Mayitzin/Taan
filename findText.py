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
# import skimage.filters.laplace as laplace

# Load image
page = scimg.imread('page001.png')

# Filter image
sharpened_page = scimg.filters.laplace(page)

# Show images
plt.subplot(1,2,1)
plt.imshow(page)
plt.subplot(1,2,2)
plt.imshow(sharpened_page)

# Show image
plt.show()