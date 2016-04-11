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
import scipy.signal as sig
import numpy as np

# Load image in gray-scale
page = (255-scimg.imread('page001.png', flatten=True))/255.0
print np.shape(page), "\n", np.min(page), "\n", np.max(page)

# Filter image
# mask = np.array([[-0.090909, -0.818182, -0.090909],
#                  [-0.818182,  4.636364, -0.818182],
#                  [-0.090909, -0.818182, -0.090909]])
# sharpened_page = scimg.filters.convolve(page, mask, mode='reflect')
sharpened_page = scimg.filters.gaussian_laplace(page, 1.0)
min_sharp = np.min(sharpened_page)
max_sharp = np.max(sharpened_page)
print np.shape(sharpened_page), "\n", min_sharp, "\n", max_sharp

# Histogram of Image
hist = scimg.measurements.histogram(sharpened_page, min_sharp, max_sharp, 255)

# Binarization of Image
threshold = 0.004
sharpened_page[sharpened_page>threshold] = 1.0
sharpened_page[sharpened_page<=threshold] = 0.0
print np.shape(sharpened_page), "\n", np.min(sharpened_page), "\n", np.max(sharpened_page)

# Show images
plt.subplot(1,3,1)
plt.imshow(page, cmap='Greys')
plt.subplot(1,3,2)
plt.plot(np.linspace(min_sharp, max_sharp, num=255),hist)
plt.subplot(1,3,3)
plt.imshow(sharpened_page, cmap='Greys')

# Show image
plt.show()