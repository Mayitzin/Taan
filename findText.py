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
from scipy import misc
import numpy as np
import copy

# Load image in gray-scale
page = (255-scimg.imread('page001.png', flatten=True))/255.0
print np.shape(page), "\n", np.min(page), "\n", np.max(page)

# Filter image
# mask = np.array([[-0.090909, -0.818182, -0.090909],
#                  [-0.818182,  4.636364, -0.818182],
#                  [-0.090909, -0.818182, -0.090909]])
# sharpened_page = scimg.filters.convolve(page, mask, mode='reflect')
sharpened_page = scimg.filters.gaussian_laplace(page, 0.85)
min_sharp = np.min(sharpened_page)
max_sharp = np.max(sharpened_page)
print np.shape(sharpened_page), "\n", min_sharp, "\n", max_sharp


# Binarization of Image
threshold = -0.004
binary_img = copy.copy(sharpened_page)
binary_img[binary_img>threshold] = max_sharp
binary_img[binary_img<=threshold] = min_sharp
binary_img[binary_img==max_sharp] = 0.0
binary_img[binary_img==min_sharp] = 1.0
print np.shape(binary_img), "\n", np.min(binary_img), "\n", np.max(binary_img)

# Save Image
misc.imsave('outfile.png', binary_img)

# Show images
plt.subplot(1,3,1)
plt.imshow(page, cmap='Greys')
plt.subplot(1,3,2)
plt.imshow(sharpened_page, cmap='Greys')
plt.subplot(1,3,3)
plt.imshow(binary_img, cmap='Greys')

# Show image
plt.show()