async function test() {
    const sess = new onnx.InferenceSession()
    await sess.loadModel('./data/models/segmentation_model.onnx')
    const input = new onnx.Tensor(new Float32Array(256*256), 'float32', [1, 3, 256, 256])
    const outputMap = await sess.run([input])
    const outputTensor = outputMap.values().next().value
    console.log("here")
    console.log(`Output tensor: ${outputTensor.data}`)
}
test()