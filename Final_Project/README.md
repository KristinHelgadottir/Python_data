# Pattern recognition with machine learning.


Image and pattern recognition can allow computers to translate written text on paper into digital text, 
it can help machine vision, robots and other devices to recognize people and objects or areas.  
Data Mining - process of analyzing data from different perspectives and summarizing it into useful information.  


![alt tag](https://behavior.lbl.gov/sites/behavior.lbl.gov/files/data_mining.png)


### Goal
Our goal is to use machine learning, in the form of pattern recognition, to teach our program how to recognise different
abstract shapes and calculate relation between the values in the shape and indifferences.  
Is there indifferences (in color?) in the shape/image and if yes, what kind and how big. Possible plotting :)


![alt tag](https://static.wixstatic.com/media/e4cc5f_5553e39727ac4ce1ab9179a0f3bff452~mv2.png/v1/fill/w_561,h_198,al_c,usm_0.66_1.00_0.01/e4cc5f_5553e39727ac4ce1ab9179a0f3bff452~mv2.png)

From https://orbitalinsight.com/solutions/agriculture/


### Steps we need to do:
1. Getting sample documents/images and placing the "sample_images" folder where the script will be. Within that folder, we have some simple images with shapes, that we'll be using to feed the machine learning.

2. Once we have sample data, we're going to need the Python programming language, we are using Python 3. Set up the work enviorement with importing the nececary modules and open the image using our image processor.
```Python
from PIL import Image
import numpy as np

i = Image.open('sample_images/dot.png')
etc...
```
3. Opening image as 3-dimensional array of the data. The higher the number, the more solid the color is, the lower the number, the more transparent it is.  

4. TODO


### Packages we will use:
* TensorFlow - for machine learning. 
* Matplotlib - package for plotting. 
* Numpy - package for mathematical calculations. 
* MeanShift, KMeans for finding colour clusters. 
* OpenCV - computer vision and machine learning software library. 
* Pillow - Python Imaging Library ?

