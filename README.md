<center><h1>T'aan</h1></center>

This project intends to easily recognize characters in old writings and automatically translate them to any other language.

## Usage

```
python img2txt.py <input_file> <output_file>
```

## Requirements

* [Tesseract](https://github.com/tesseract-ocr/tesseract) by Google is used by T'aan to perform the OCR. Download it or clone it from its repository in GitHub. Follow the [installing instructions](https://github.com/tesseract-ocr/tesseract/wiki) for your corresponding OS. The latest version already includes models to recognize the most common writing systems and languages.

* The module [pdf2image](https://github.com/Belval/pdf2image), a wrapper of [poppler](https://poppler.freedesktop.org/), is required to transform a given PDF into images and then use Tesseract.

## References

### Online

* [OCRchie: Modular Optical Character Recognition Software](http://www.cs.berkeley.edu/~fateman/kathey/ocrchie.html). An OCR software package created by Katherine Marsden, while a Computer Science graduate from the Univerity of Berkeley in 1996.
* [Character Recognition by Feature Point Extraction](http://www.ccs.neu.edu/home/feneric/charrec.html). An old but entertaining approach to detect characters based on feature points created by Eric W. Brown of the Northeastern University in 1992.
* [Optical Character Recognition](http://www.codeproject.com/Articles/476142/Optical-Character-Recognition). A short description of a simple OCR by Vijay Rajan Nadar using pixel counting and relative location.
* [Automatically Detect and Recognize Text in Natural Images](http://de.mathworks.com/help/vision/examples/automatically-detect-and-recognize-text-in-natural-images.html). An example using MATLAB to detect regions containing text in an image.
* [Neural Network OCR](http://www.codeproject.com/Articles/11285/Neural-Network-OCR). Some ideas about optical character recognition using neural networks presented in an article by Andrew Kirillow. 2005.
* [CNNs for handwritten and machine-printed character recognition](http://yann.lecun.com/exdb/lenet/). An example of Convolutional Neural Networks designed to recognize visual patterns directly from pixel images with minimal preprocessing.
* [Coding Bilinear Interpolation](http://supercomputingblog.com/graphics/coding-bilinear-interpolation/). A short explanation and the code for a Bilinear Interpolation by The Supercomputing Blog.
* [Fast C++: Bilinear Pixel Interpolation using SSE](http://fastcpp.blogspot.de/2011/06/bilinear-pixel-interpolation-using-sse.html). Explanation and code for a fast Bilinear interpolation implemented in C++.
* [OpenCV Tutorials](http://docs.opencv.org/master/d9/df8/tutorial_root.html#gsc.tab=0). Set of basic OpenCV tutorials.

### Books and Articles

* M. Cheriet, N. Kharma, C. Liu and C. Suen. _Character Recognition Systems: A Guide for Students and Practitioners_. John Wiley & Sons. 2007.
* H. Bunke and P.S.P. Wang. _Handbook of Character Recognition and Document Image Analysis_. World Scientific Pub Co Inc. 1997.
* S.V. Rice, G. Nagy and T.A. Nartker. _Optical Character Recognition: An Illustrated Guide to the Frontier (The Springer International Series in Engineering and Computer Science)_. Springer. 1999.
* C. Steger, M. Ulrich and C. Wiedemann. _Machine Vision: Algorithms and Applications_. Wiley-VCH. 2007.
* C.M. Bishop. _Neural Networks for Pattern Recognition (Advanced Texts in Econometrics_. Clarendon Press. 1st Edition. 1996.
* D.L. Baggio, S. Emami, D.M. Escrivá, K. Ievgen, N. Mahmood, J. Saragih, R. Shilkrot. _Mastering OpenCV with Practical Computer Vision Projects_. Packt Publishing. Pages 176-187. 2012.
* J. Gllavata, R. Ewerth and B. Freisleben. [_A Robust Algorithm for Text Detection in Images_](http://saigo.googlecode.com/svn/trunk/papers/artigos1/globalthr.pdf). Proceedings of the 3rd International Symposium on Image and Signal Processing and Analysis 2003. Volume 2. Pages 611-616.
* W. Huang., Z. Lin, J. Yang, and J. Wang. [_Text Localization in Natural Images using Stroke Feature Transform and Text Covariance Descriptors_](http://www.wlhuang.com/papers/whuang2013_iccv.pdf)_. IEEE International Conference on Computer Vision (ICCV), 2013.
* L. Kang, Y. Li and D. Doermann. [_Orientation Robust Text Line Detection in Natural Images_](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Kang_Orientation_Robust_Text_2014_CVPR_paper.pdf). CVPR2014.
* F. Mohammad, J. Anarase, M. Shingote and P. Ghanwat. [_Optical Character Recognition Implementation Using Pattern Matching_](http://www.ijcsit.com/docs/Volume%205/vol5issue02/ijcsit20140502254.pdf). International Journal of Computer Science and Information Technologies. Volume 5 (2). pages 2088-2090. 2014.
* O.D Trier, A.K. Jain and T. Taxt. [_Feature Extraction Methods for Character Recognition - A Survey_](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.51.7439&rep=rep1&type=pdf). Patter Recognition. Volume 29. Issue 4. Pages 641-662. April 1996.
* R. Lienhart and A. Wernicke. [_Localizing and Segmenting Text in Images and Videos_](http://www.lienhart.de/Prof._Dr._Rainer_Lienhart/Publications_files/lienhart-csvt2002.pdf). IEEE Transactions on Circuits and Systems for Video Technology. Volume 12. Issue 4. April 2002.
* Y. Amit and D. Geman [_Shape Quantization and Recognition with Randomized Trees_](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.102.5478&rep=rep1&type=pdf). Neural Computation. Volume 9. Pages 1545-1588. 1997.

---

## What is T'aan?

T'aan means _language_ in Mayan. In pre-hispanic [Mesoamerica](https://en.wikipedia.org/wiki/Mesoamerica) existed dozens of languages and hundreds of dialects, which difficulted the fast integration of the several nations. In order to ease their communication, specialized translators and interpreters were established. These interpreters could read the several scripts and codices and, thus, connect their communities.

The Mayans of Yucatán used the word **T'aan** to name _language_, _conversation_, _to read aloud_, _word_ or _voice_. In short, everything that had to do with communication in any language belongs to the space of **T'aan**.
