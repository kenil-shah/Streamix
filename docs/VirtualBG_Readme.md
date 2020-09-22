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

# Reference
- [1] [Fast Deep Matting for Portrait Animation on Mobile Phone](https://arxiv.org/pdf/1707.08289.pdf)
