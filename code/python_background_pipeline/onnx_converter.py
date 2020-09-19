import torch
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Model conversion (Torch -> ONNX)')
    parser.add_argument('--modelpath',
                         default='./data/models/segmentation_model.pth',
                         help='Location of pytorch model')
    parser.add_argument('--dummyinputsize',
                         default=[1, 3, 256, 256],
                         help='Default input shape for model')
    parser.add_argument('--opset',
                        default=int(10),
                        help='Operator Set version for ONNX conversion')
    parser.add_argument('--savepath',
                         default='./data/models/segmentation_model.onnx',
                         help='Path where you want to save onnx model')

    args = vars(parser.parse_args())

    model = torch.load(args['modelpath'], map_location= lambda storage, loc: storage)
    shape = args['dummyinputsize']
    print(type(shape[0]))
    dummy_input = torch.randn(shape[0], shape[1], shape[2], shape[3])
    torch.onnx.export(model, dummy_input, args['savepath'], opset_version=int(args['opset'])) 

