function init() {
  video = document.getElementById("video")
  vendorUrl = window.URL || window.webkitURL;
  navigator.getMedia = navigator.getUserMedia ||
                      navigator.webkitGetUserMedia ||
                      navigator.mozGetUserMedia ||
                      navigator.maGetUserMedia;
  navigator.getMedia({
      video: { width: 800, height: 450},
      audio: false
  }, function(stream){
      video.srcObject = stream;
  }, function(error){
      alert("error occured")
  });

  can = document.getElementById('output-canvas');
  can_context = can.getContext('2d');

  video.addEventListener('play', computeFrame );
}

function computeFrame() {
    can_context.drawImage(video, 0, 0, video.videoWidth , video.videoHeight );
    setTimeout(computeFrame, 0);
}

document.addEventListener("DOMContentLoaded", () => {
  init();
});