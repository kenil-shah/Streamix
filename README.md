# Streamix :- Enhancing Video Conferencing Platforms

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4033418.svg)](https://doi.org/10.5281/zenodo.4033418)
[![Build Status](https://travis-ci.com/kenil-shah/Streamix.svg?branch=master)](https://travis-ci.org/kenil-shah/Streamix)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![YouTube Video Views](https://img.shields.io/youtube/views/2DVQ2XwhtUI?style=social)

# About Streamix
Streamix is a video conferencing feature that provides you seamless virtual background matting regardless of your surroundings and provides you eye gaze correction thus giving you a feeling of a natural face to face interaction. We have used python to develop virtual background mating model and we are using ReactJS and NodeJS to build a webapp where you can see the power of our algorithms.

[![Watch the video](https://i.ytimg.com/vi/2DVQ2XwhtUI/hqdefault.jpg)](https://www.youtube.com/watch?v=2DVQ2XwhtUI)


# Installation
1. Clone Streamix Repo
2. From the root directory run the following command
```
pip install -r requirements.txt
```

# Usage
1. Go to code directory and run the following command.
```
python server.py
```
2. Run the docker file
```
docker build --tag my-python-app .
docker run --name python-app -p 5000:5000 my-python-app
```
# How to Contribute?
Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and help us in enhancing the current video conferencing platforms.

# What things have been done for Phase1?
* Implemented the segmentation algorithm discussed in this [paper](https://arxiv.org/pdf/1707.08289.pdf).
* Trained the above-mentioned model for accurately locating the person in the video.
* Did some experimentations with inference to speedup the algorithm (Current speed 25FPS).
* Created a GUI using Tkinter for locally running the application.
* Created a dummy fronted using NodeJS so that team in Phase2 can use this code as a reference.
* Basic Fronted features such as selecting the Virtual BG.
* Sending the images as response to the front end.
* Rendering the images with Virtual BG on the front end.
* Implemented the basic code for EyeGaze Correction but inference is very slow and not worth the deployment.

# What is the plan for Phase2? 
* Improvise the front end for the application and add more features and functionalities to the same.
* Create a pluging for Zoom using the above code as reference.
* Try to render the eyegaze corrected images faster and if possible achieve the speed of around 10FPS.
* Use some opensource video conferencing platforms and merge the above two features in that application.

# Documentation
1. Documentation for the [Segmentation Algorithm](https://github.com/kenil-shah/Streamix/blob/master/docs/Segmentation_Readme.md)
2. Documentation for the [Virtual Background](https://github.com/kenil-shah/Streamix/blob/master/docs/VirtualBG_Readme.md)
3. Documentation for the [LocalGUI implemetation details](https://github.com/kenil-shah/Streamix/blob/master/docs/LocalGUI_Readme.md)
4. Documentation for the [Flask implemetation details](https://github.com/kenil-shah/Streamix/blob/master/docs/FlaskServer_Readme.md)
5. Documentation for the [EyeGaze Correction details](https://github.com/kenil-shah/Streamix/blob/master/docs/EyeGaze_Readme.md)
