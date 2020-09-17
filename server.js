const onnx = require('onnxjs');
const http = require('http');
const express = require('express');
const app = express();
const server = http.createServer(app);
const WebAssembly = require('webassembly');


app.get('/', (req, res) => {
 function test() {
    const sess = new onnx.InferenceSession();
    sess.loadModel('./data/models/segmentation_model.onnx');
    const input = new onnx.Tensor(new Float32Array(256*256), 'float32', [1, 3, 256, 256]);
    const outputMap = sess.run([input]);
    const outputTensor = outputMap.values().next().value();
    console.log(`Output tensor: ${outputTensor.data}`);
  };
  test();
});

server.listen(8888);
