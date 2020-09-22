# About Segmentation Algorithm
We have implement a CNN based Segmentation algorithm which is capable of giving binary class for every person.
At the output end of this algorithm, we will have a floating point value between 0 to 1 for every single pixel in the image.
We will pre-define a specific threshold value and if a particular pixel is less than that value, then we will consider it
as a background.

![Alt Text](https://github.com/kenil-shah/Streamix/blob/master/data/readme_files/model_description.PNG)

#Location of Code
The code that implements the above mentioned Segmentation algorithm is located in
```
code/python_background_pipeline/net/segnet.py
```

# Code Description
## Classes
1. ResidualDenseBlock():

2. SegMattingNet()

# Reference
- [1] [Fast Deep Matting for Portrait Animation on Mobile Phone](https://arxiv.org/pdf/1707.08289.pdf)