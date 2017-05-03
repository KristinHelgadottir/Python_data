# Pattern recognition with machine learning.


Image and pattern recognition can allow computers to translate written text on paper into digital text, 
it can help machine vision, robots and other devices to recognize people and objects or areas.  
Data Mining - The process of analyzing data from different perspectives and summarizing it into useful information.  


![alt tag](https://behavior.lbl.gov/sites/behavior.lbl.gov/files/data_mining.png)


### Goal
Our goal is to use machine learning, in the form of pattern recognition, to teach our program how to recognise faces and calculate relation between the pigment indifferences in face and wich faces are recognized faster.  



Is there indifferences (in color?) and if yes, what kind and how big. Possible plotting :)


![alt tag](https://images.duckduckgo.com/iu/?u=https%3A%2F%2Fsophosnews.files.wordpress.com%2F2015%2F02%2Fface-detection_550.jpg%3Fw%3D640&f=1)



### Steps we need to do:
1. Getting sample documents/images and placing the "sample_images" folder where the script will be. Within that folder, we have some simple images with shapes, that we'll be using to feed the machine learning.

2. Once we have sample data, we're going to need the Python programming language, we are using Python 3. Set up the work enviorement with importing the nececary modules and open the image using our image processor.
```Python
from PIL import Image
import numpy as np

etc...
```
3. TODO


### Packages we will use:
* TensorFlow - for machine learning. 
* Matplotlib - package for plotting. 
* Numpy - package for mathematical calculations. 
* MeanShift, KMeans for finding colour clusters. 
* OpenCV - computer vision and machine learning software library. 
* Pillow - Python Imaging Library ?
* Thresholding - thresholding any pixel as black if it is any darker or white if it is lighter then average ?
