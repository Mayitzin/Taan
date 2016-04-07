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
page = scimg.imread('page001.png', flatten=True)

# Filter image
sharpened_page = scimg.filters.gaussian_laplace(page, 0.1)

# Show images
plt.subplot(1,2,1)
plt.imshow(page, cmap='Greys')
plt.subplot(1,2,2)
plt.imshow(sharpened_page, cmap='Greys')

# Show image
plt.show()