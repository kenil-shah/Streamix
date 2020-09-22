# About VirtualBG
The primary input to the virtual background alogorithm would be a normal image captured from the webcamera.
This input image would first of all pass from the segmentation pipeline. The  output of the segmentation pipeline would be 
a binary mask of the input image. In this mask, white pixels would denote the presence of a person (foreground) and the black pixels
would denote the presence of background. This binary mask would be the input for our Image matting algorithm where we matt 
the masked image with the original input image and backgroun image selected by the user.

![Alt Text](https://github.com/kenil-shah/Streamix/blob/master/data/readme_files/result.jpeg)

**Results.**

#Location of Code
The code that implements the above mentioned Segmentation algorithm is located in
```
code/python_background_pipeline/segmenter.py
```

# Code Description

## Python Packages
1. segmenter.py

## Classes
1. get_segmentation()

There are 6 methods inside this class:

1. __init__

Initializes the object variables with the values passed from the argument parser

2. load_background

Input: None

Output: Image

Reads the background image that was passed as an argument and returns it after some transformation. Used to initialize an object variable with the background image

3. load_model

Input: None

Output: Segnet Model

Fetches the segnet.py model and returns it. Used to store the model inside the class

4. seg_process

Input: Image, Segnet Model

Output: Image, Image

Takes the image and model as input, passes the image through the model and decides the foreground(human) potion and background potion of the image via a threshold passed as argument to the class. Returns the foreground part and background part of the image and in the exact order

5. matt_background

Input: Image, Image, Image

Output: Array

Takes the foreground potion, background potion and overall image. Converts the image to an array containing black and white pixels that are determined by the foreground and background images

6. run_torch

Input: Image

Output: None

Takes a frame and splits it into foreground and background potion. Then returns an array consisting of black and white pixels

# Reference
- [1] [Fast Deep Matting for Portrait Animation on Mobile Phone](https://arxiv.org/pdf/1707.08289.pdf)
