var socket=io();
var status = document.getElementById("status");

function load_StudyTable() {
    imageUrl = "StudyTable.jpg";
    socket.emit('bgimage', imageUrl);
    status.innerHTML = "Background selected";
}
function load_sfbridge(){
    imageUrl = "sf_bridge.jpg";
    socket.emit('bgimage', imageUrl);
    status.innerHTML = "Background selected";
}

function load_HomeBG2(){
    imageUrl = "HomeBG2.jpg";
    socket.emit('bgimage', imageUrl);
    status.innerHTML = "Background selected";
}

function load_HomeBG(){
    imageUrl = "HomeBG.jpg";
    socket.emit('bgimage', imageUrl);
    status.innerHTML = "Background selected";
}

function load_EmpireState(){
    imageUrl = "EmpireState.png";
    socket.emit('bgimage', imageUrl);
    status.innerHTML = "Background selected";
}
