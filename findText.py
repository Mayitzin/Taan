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
page = scimg.imread('page001.png', flatten=True)/255.0
print np.shape(page), "\n", np.min(page), "\n", np.max(page)

# Filter image
mask = np.array([[-0.090909, -0.818182, -0.090909],
                 [-0.818182,  4.636364, -0.818182],
                 [-0.090909, -0.818182, -0.090909]])
# sharpened_page = scimg.filters.convolve(page, mask, mode='reflect')
sharpened_page = scimg.filters.gaussian_laplace(page, 0.5)
print np.shape(sharpened_page), "\n", np.min(sharpened_page), "\n", np.max(sharpened_page)

# Show images
plt.subplot(1,2,1)
plt.imshow(page, cmap='Greys')
plt.subplot(1,2,2)
plt.imshow(sharpened_page, cmap='Greys')

# Show image
plt.show()