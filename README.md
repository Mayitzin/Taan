# Fraktur OCR

This project is to build an OCR for Fraktur typefaces.

* Should it use OCR Tesseract?
* Should it use parts of it?
* Should it be built from zero?

# Overview

1. Read Image in gray-scale. If not in gray-scale then [transform it to gray-scale](https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale) in terms of the CIE 1931.
2. Identify Orientation. The direction of the lines with text must be aligned with the horizontal Axis of the image. Probably a binarization of the image is needed here to create a histogram.
3. Rectify Image with an [affine Transformation](http://docs.opencv.org/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html), or [projective transformation](http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/BEARDSLEY/node3.html) for severe cases.
4. [Bilinear Interpolation](https://en.wikipedia.org/wiki/Bilinear_interpolation) (to avoid losing detail) with a Gaussian smoothing if needed.
5. [Binarization](http://www.leptonica.com/binarization.html) of the image.
6. Vertical dilation to join dots of 'i' and 'j', and umlauts.
7. Segmentation of each character.
  * Width is not constant.
  * Specify possible dimensions (height and width).
  * Dynamic estimation of dimensions.
8. Character normalization.
  * Moment based.
  * Contour Tracing/Analysis.
9. Feature extraction.
  * Anisometry.
  * Ratio between height/width.
  * Number of holes.
  * From skeleton (after thinning).
  * PCA for dimensionality reduction.
  * etc.
10. Classify character.
  * Classification methods.
    * Random trees.
    * Support Vector Machines.
    * kNNs.
    * Multilayer Perceptron.
    * Neural Networks.
    * Convolutional Neural Networks.
  * Optimization.
    * Boosting.
    * Ensemble methods?
    * Conext-based classification.

# References

## Online

* [Fraktur](https://en.wikipedia.org/wiki/Fraktur). Resource from Wikipedia.
* [Chart of Fraktur](http://www.library.yale.edu/cataloging/music/fraktur.htm). A chart with all the characters in English. It misses letters with umlaut.
* [OCRchie: Modular Optical Character Recognition Software](http://www.cs.berkeley.edu/~fateman/kathey/ocrchie.html). An OCR software package created by Katherine Marsden, while a Computer Science graduate from the Univerity of Berkeley in 1996.
* [Character Recognition by Feature Point Extraction](http://www.ccs.neu.edu/home/feneric/charrec.html). An old but entertaining approach to detect characters based on feature points created by Eric W. Brown of the Northeastern University in 1992.
* [Optical Character Recognition](http://www.codeproject.com/Articles/476142/Optical-Character-Recognition). A short description of a simple OCR by Vijay Rajan Nadar using pixel counting and relative location.
* [Automatically Detect and Recognize Text in Natural Images](http://de.mathworks.com/help/vision/examples/automatically-detect-and-recognize-text-in-natural-images.html). An example using MATLAB to detect regions containing text in an image.
* [Neural Network OCR](http://www.codeproject.com/Articles/11285/Neural-Network-OCR). Some ideas about optical character recognition using neural networks presented in an article by Andrew Kirillow. 2005.
* [CNNs for handwritten and machine-printed character recognition](http://yann.lecun.com/exdb/lenet/). An example of Convolutional Neural Networks designed to recognize visual patterns directly from pixel images with minimal preprocessing.
* [Coding Bilinear Interpolation](http://supercomputingblog.com/graphics/coding-bilinear-interpolation/). A short explanation and the code for a Bilinear Interpolation by The Supercomputing Blog.
* [Fast C++: Bilinear Pixel Interpolation using SSE](http://fastcpp.blogspot.de/2011/06/bilinear-pixel-interpolation-using-sse.html). Explanation and code for a fast Bilinear interpolation implemented in C++.
* [OpenCV Tutorials](http://docs.opencv.org/master/d9/df8/tutorial_root.html#gsc.tab=0). Set of basic OpenCV tutorials.

## Books and Articles

* **Book**: M. Cheriet, N. Kharma, C. Liu and C. Suen. _Character Recognition Systems: A Guide for Students and Practitioners_. John Wiley & Sons. 2007.
* **Book**: H. Bunke and P.S.P. Wang. _Handbook of Character Recognition and Document Image Analysis_. World Scientific Pub Co Inc. 1997.
* **Book**: S.V. Rice, G. Nagy and T.A. Nartker. _Optical Character Recognition: An Illustrated Guide to the Frontier (The Springer International Series in Engineering and Computer Science)_. Springer. 1999.
* **Book**: C. Steger, M. Ulrich and C. Wiedemann. _MAchine Vision: Algorithms and Applications_. Wiley-VCH. 2007.
* **Book**: C.M. Bishop. _Neural Networks for Pattern Recognition (Advanced Texts in Econometrics_. Clarendon Press. 1st Edition. 1996.
* **Book**: D.L. Baggio, S. Emami, D.M. Escrivá, K. Ievgen, N. Mahmood, J. Saragih, R. Shilkrot. _Mastering OpenCV with Practical Computer Vision Projects_. Packt Publishing. Pages 176-187. 2012.
* J. Gllavata, R. Ewerth and B. Freisleben. [_A Robust Algorithm for Text Detection in Images_](http://saigo.googlecode.com/svn/trunk/papers/artigos1/globalthr.pdf). Proceedings of the 3rd International Symposium on Image and Signal Processing and Analysis 2003. Volume 2. Pages 611-616.
* W. Huang., Z. Lin, J. Yang, and J. Wang. [_Text Localization in Natural Images using Stroke Feature Transform and Text Covariance Descriptors_](http://www.wlhuang.com/papers/whuang2013_iccv.pdf)_. IEEE International Conference on Computer Vision (ICCV), 2013.
* L. Kang, Y. Li and D. Doermann. [_Orientation Robust Text Line Detection in Natural Images_](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Kang_Orientation_Robust_Text_2014_CVPR_paper.pdf). CVPR2014.
* F. Mohammad, J. Anarase, M. Shingote and P. Ghanwat. [_Optical Character Recognition Implementation Using Pattern Matching_](http://www.ijcsit.com/docs/Volume%205/vol5issue02/ijcsit20140502254.pdf). International Journal of Computer Science and Information Technologies. Volume 5 (2). pages 2088-2090. 2014.
* O.D Trier, A.K. Jain and T. Taxt. [_Feature Extraction Methods for Character Recognition - A Survey_](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.51.7439&rep=rep1&type=pdf). Patter Recognition. Volume 29. Issue 4. Pages 641-662. April 1996.
* R. Lienhart and A. Wernicke. [_Localizing and Segmenting Text in Images and Videos_](http://www.lienhart.de/Prof._Dr._Rainer_Lienhart/Publications_files/lienhart-csvt2002.pdf). IEEE Transactions on Circuits and Systems for Video Technology. Volume 12. Issue 4. April 2002.
* Y. Amit and D. Geman [_Shape Quantization and Recognition with Randomized Trees_](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.102.5478&rep=rep1&type=pdf). Neural Computation. Volume 9. Pages 1545-1588. 1997.