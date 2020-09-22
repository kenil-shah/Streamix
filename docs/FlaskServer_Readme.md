# About Flask Application

During the development phase of algorithm, we used the virtual background application implemented using TKinter which allowed 
us to asses the performance of our code locally. Major goal of this project is to integrate this feature with open source video 
conferencing application. So, we come up with a solution to develop a flask application which hosts the server locally 
and users can connect using the URL from their web browsers. 

Main purpose behind hosting this server is to analyse the performance of the developed algorithm when there is another overhead 
of time for sending frame between client and server continuously. This is important since testing algorithm using local GUI
application does not consider this additional lag. 

![Alt Text](https://github.com/kenil-shah/Streamix/blob/master/data/readme_files/flask_demo.png)

## approach

As of now, we are transmitting an image from client to server every 40 millisecond. Server processes the image using our 
algorithm and sends it back to the client to render. We are not seeing any lag with this chosen interval which makes our
algorithm perform perfectly with 23-25 frames per second.

For continuous and bi-directional communication between client and server, we've chosen web sockets instead of normal HTTP
requests. Images are transmitted in the Base64 encoded format back and forth between client and server.

## Code Description

1. ```code/server.py``` implements the main server logic. 
2. ```code/templates/index.html``` represents the main webpage user will interact with.
3. ```code/static/js/script.js``` handles the requests to the server and collects the images back.

### server.py
1. ```handle_request()``` method provides the main webpage to users when they send initial request to the server.
2. ```handle_image()``` method is called whenever client sends a frame to the server for segmentation. This method takes ```data``` as input 
which is data transmitted from the client and sends the segmented image back. These images are encoded as Base64 byte data.
3. ```get_args()``` method initializes the parameter for segmentation class ```get_segmentation```.

### index.html
There are 4 main elements of this page:
1. ```video tag```: shows the input from clients web cam.
2. ```image tag```: shows the output from the implemented algorithm.
3. ```output frame count```: shows the frame number that is being sent to the server.
4. ```input frame count```: shows the frame number that is being received from the server.

Our goal is to find an optimal value for interval with which frames are beings sent such that difference between output frame count and input frame count is as little as possible.

### script.js
1. ```init()``` function asks user for permission to access the webcam, initilizes video element with webcam video stream and calls ```compute_frame()``` to start sending frames over.
2. ```compute_frame()``` function captures the frame from the video element and send it to the server. This function calls itself after every 40 milliseconds.
3. ```socket.on()``` function accepts output frames from the server and displays it in the image element.

