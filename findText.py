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
import copy

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
hist = scimg.measurements.histogram(sharpened_page, min_sharp, max_sharp, 256)

# Binarization of Image
threshold = -0.004
binary_img = copy.copy(sharpened_page)
binary_img[binary_img>threshold] = max_sharp
binary_img[binary_img<=threshold] = min_sharp
binary_img[binary_img==max_sharp] = 1.0
binary_img[binary_img==min_sharp] = 0.0
print np.shape(binary_img), "\n", np.min(binary_img), "\n", np.max(binary_img)
print 256.0/np.argmax(hist)

# Show images
plt.subplot(1,4,1)
plt.imshow(page, cmap='Greys')
plt.subplot(1,4,2)
plt.imshow(sharpened_page, cmap='Greys')
plt.subplot(1,4,3)
plt.plot(np.linspace(min_sharp, max_sharp, num=256),hist)
plt.subplot(1,4,4)
plt.imshow(binary_img, cmap='Greys')

# Show image
plt.show()