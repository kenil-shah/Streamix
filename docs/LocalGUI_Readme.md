# About Local GUI
In order to run the Virtual Background Application locally, we have added the a
Graphical User Interface using Tkinter in python. The user will have the ability to select from the two methods,
1. Run Normal Webcam:
2. Run Virtual Background:


![Alt Text](https://github.com/kenil-shah/Streamix/blob/master/data/readme_files/localGUI.PNG)

#Location of Code
The code that implements the above mentioned Segmentation algorithm is located in
```
code/python_background_pipeline/tkGUI/
```

# Code Description
## Python Packages
## 1. app.py:
#### App() 
Usage :- This Class is used for initiating our Tkinter Graphical User interface. 
It is define the whole GUI, instantiate the process manager and run the whole GUI in an infinite loop. 

## 2. data_bridge.py
#### Data_bridge()

Usage :- This class is used as way to pass variables between various other classes. Different variables such as image path,
start process, stop process etc.
 
## 3. gui_creator.py
#### Gui_creator() 

Usage :- This class is used to define our whole GUI. Various features such a start button, stop button, video file fetching,
method selection etc. are defined by using this class. This class also fetches the value of variables from the data_bridge for the processing 
of the application. Moreover, it is also responsible for location of buttons on different rows/columns of the application.
 
## 4. methods.py
#### Raw_video()

Usage :- This class implements the first method of the application. In this method user gets the camera view without 
anysort of Virtual Background. It has a function main_thread which runs the webcam till the user presses the stop processing button from the application. 

#### Virtual_BG():

Usage :- This class implements the second method of the application. In this method user gets the camera view with 
the Virual Background that he/she has asked for in the begining. It has a function main_thread which runs the webcam till the user presses the stop processing button from the application.
  

## 5. process_manager.py
#### Process_manager()

Usage :- This class acts a response for various different buttons pressed on the GUI. Every time a button is pressed, this class reinitiates the variable value
in the data_bridge class. Later, by using that data_bridge class we will be calling different methods as per the users request.

# Reference
- [1] [Use Tkinter for Python GUI](https://docs.python.org/3/library/tkinter.html)


