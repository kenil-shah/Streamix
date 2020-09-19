const express = require('express')
const app = express()
const path = require('path')
const server = require('http').Server(app)
const io = require('socket.io')(server)

const PORT = 5000;

app.use(express.static(path.resolve(__dirname,'../public')));

server.listen(PORT, ()=> console.log('server is listening on port ' + PORT))