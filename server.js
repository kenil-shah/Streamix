const http = require('http');
const express = require('express');
const app = express();
const server = http.createServer(app);
const onnx = require("onnxjs");
const sess = new onnx.InferenceSession('cpu');

app.get('/', (req, res) => {
  async function test() {
    await sess.loadModel('./data/models/segmentation_model11.onnx');
    const input = new onnx.Tensor(new Float32Array(256*256*3), 'float32', [1, 256, 256, 3]);
    const outputMap = await sess.run([input]);
    const outputTensor = outputMap.values().next().value();
    console.log(`Output tensor: ${outputTensor.data}`);
  };
  test()
});

server.listen(8888);
