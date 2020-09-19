# Running onnx converter
    
    python onnx_converter.py --modelpath "path_to_saved_model/modelname.pth" --opset OP_VERSION --savepath "path_where_to_save_converted_model/modelname.onnx"

### Example 
    python onnx_converter.py --modelpath '/home/hpatel24/Fall2020/CSC510/project1/Streamix/data/models/segmentation_model.pth' --opset 10 --savepath '/home/hpatel24/Fall2020/CSC510/project1/Streamix/data/models/segmentation_model11.onnx'


