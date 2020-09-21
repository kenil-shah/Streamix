import cv2
import torch
import torch.onnx
torch.set_grad_enabled(False)
import argparse
import numpy as np
import warnings
warnings.filterwarnings("ignore")
#from python_background_pipeline.model.segnet import SegMattingNet
from model.segnet import SegMattingNet
"""
TODO: Onnx Inference Code
"""


class get_segmentation(object):

    def __init__(self,args):
        self.model = args["model"]
        self.without_gpu = args["without_gpu"]
        self.background_image = args["background_image"]
        self.INPUT_SIZE = args["input_resolution"]
        self.device = torch.device('cpu')
        self.camera = args["camera_id"]
        self.threshold = args["threshold"]
        self.camera_res = args["camera_resolution"]
        self.background_image = self.load_background()
        self.myModel = self.load_model()

    def load_background(self):
        image = cv2.imread(self.background_image)
        image = cv2.resize(image, (self.camera_res[0], self.camera_res[1]), interpolation=cv2.INTER_CUBIC)
        return image

    def load_model(self):
        myModel = SegMattingNet()
        myModel.load_state_dict(torch.load(self.model),strict=False)
        #myModel = torch.load(self.model, map_location=lambda storage, loc: storage)
        #torch.save(myModel.state_dict(), "C:/Users/Kenil/Desktop/Github/Streamix/data/models/only_par.pth")
        myModel.eval()
        myModel.to(self.device)

        return myModel

    def seg_process(self, image, net):
        origin_h, origin_w, c = image.shape
        image_resize = cv2.resize(image, (self.INPUT_SIZE, self.INPUT_SIZE), interpolation=cv2.INTER_CUBIC)
        image_resize = (image_resize - (104., 112., 121.,)) / 255.0
        tensor_4D = torch.FloatTensor(1, 3, self.INPUT_SIZE, self.INPUT_SIZE)
        tensor_4D[0, :, :, :] = torch.FloatTensor(image_resize.transpose(2, 0, 1))
        inputs = tensor_4D.to(self.device)
        seg, alpha = net(inputs)
        alpha_np = alpha[0, 0, :, :].data.numpy()
        fg_alpha = cv2.resize(alpha_np, (self.camera_res[0], self.camera_res[1]), interpolation=cv2.INTER_CUBIC)
        fg_alpha[fg_alpha < self.threshold] = 0
        fg_alpha[fg_alpha >= self.threshold] = 1
        bg_alpha = 1 - fg_alpha
        return fg_alpha, bg_alpha

    def matt_background(self, fg_alpha, bg_alpha, image):
        fg = np.multiply(fg_alpha[..., np.newaxis], image)
        bg = np.multiply(bg_alpha[..., np.newaxis], self.background_image)
        out = fg + bg
        out[out < 0] = 0
        out[out > 255] = 255
        out = out.astype(np.uint8)
        return out

    def convert_to_onnx(self):
        dummy_input = torch.randn(1, 3, self.INPUT_SIZE, self.INPUT_SIZE)
        torch.onnx.export(self.myModel, dummy_input, "segmentation_model.onnx")

    def run_onnx(self):
        pass

    def run_torch(self, input_frame):
        fg_alpha, bg_alpha = self.seg_process(input_frame, self.myModel)
        segmented_frame = self.matt_background(fg_alpha, bg_alpha, input_frame)
        return segmented_frame

def get_args():

    parser = argparse.ArgumentParser(description='Background Matting')
    parser.add_argument('--model',
                        default='C:/Users/Kenil/Desktop/Github/Streamix/data/models/only_par.pth',
                        help='Location of the Trained Model')
    parser.add_argument('--without_gpu', action='store_true', default=True, help='Use CPU')
    parser.add_argument('--background_image',
                        default='C:/Users/Kenil/Desktop/Github/Streamix/data/bg_images/HomeBG.jpg',
                        help='Location of Background Image')
    parser.add_argument('--input_resolution', default=256, help='Input resolution (Higher == Slower == Acccurate)')
    parser.add_argument('--camera_resolution', default=[640, 360],
                        help='Input resolution (Higher == Slower == Acccurate)')
    parser.add_argument('--camera_id', default=0, help='Camera ID to be used')
    parser.add_argument('--threshold', default=0.75, help='Set Threshold')

    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    args = get_args()
    get_seg = get_segmentation(args)
    videoCapture = cv2.VideoCapture(args["camera_id"])
    videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, args["camera_resolution"][0])
    videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, args["camera_resolution"][1])
    import time
    while True:
        ret, frame = videoCapture.read()
        start = time.time()
        output = get_seg.run_torch(frame)
        end = time.time()
        print(end-start)
        cv2.imshow("Output", output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    videoCapture.release()



