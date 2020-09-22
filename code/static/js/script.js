var socket = io();
var i = 0;
var j = 0;

function init() {
  video = document.getElementById("video")
  image_page = document.getElementById("img")
  ie = document.getElementById("i");
  je = document.getElementById("j");

  vendorUrl = window.URL || window.webkitURL;
  navigator.getMedia = navigator.getUserMedia ||
                      navigator.webkitGetUserMedia ||
                      navigator.mozGetUserMedia ||
                      navigator.maGetUserMedia;
  navigator.getMedia({
      video: { width: 640, height: 360},
      audio: false
  }, function(stream){
      video.srcObject = stream;
  }, function(error){
      alert("error occured")
  });

  can1 = document.createElement("CANVAS");
  can1.width  = 640;
  can1.height = 360;
  can1_context = can1.getContext('2d');

  video.addEventListener('play', computeFrame );
}

socket.on('new', data => {
    image_page.src = 'data:image/jpeg;base64,' + data;
    j = j+1;
    ie.innerHTML = i.toString();
    je.innerHTML = j.toString();
})

function computeFrame() {
    can1_context.drawImage(video, 0, 0, video.videoWidth , video.videoHeight );
    var data = can1.toDataURL('image/jpeg').split(';base64,')[1];
    socket.emit('image',data);
    i = i+1;
    ie.innerHTML = i.toString();
    je.innerHTML = j.toString();
    setTimeout(computeFrame, 45);
}

document.addEventListener("DOMContentLoaded", () => {
  init();
});

