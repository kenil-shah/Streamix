import cv2
import torch
import torch.onnx
torch.set_grad_enabled(False)
import argparse
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from python_background_pipeline.net.segnet import SegMattingNet
import sys


class get_segmentation(object):

    def __init__(self, args):
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
        #image = cv2.imread(self.background_image)
        image = cv2.imread("EmpireState.png")
        image = cv2.resize(image, (self.camera_res[0], self.camera_res[1]), interpolation=cv2.INTER_CUBIC)
        return image

    def load_model(self):
        myModel = SegMattingNet()
        myModel.load_state_dict(torch.load('only_params.pth'), strict=False)
#        myModel = torch.load(self.model, map_location=lambda storage, loc: storage)
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

    def run_torch(self, input_frame):
        fg_alpha, bg_alpha = self.seg_process(input_frame, self.myModel)
        segmented_frame = self.matt_background(fg_alpha, bg_alpha, input_frame)
        return segmented_frame
