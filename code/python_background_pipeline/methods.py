from data_bridge import *
from cv2 import cv2
import os
import cv2
from main import get_segmentation
import argparse
import numpy
import torch
import tkinter
import onnx
# Root directory of the project
ROOT_DIR = os.getcwd()


class Raw_video:
    def __init__(self, root):
        self.data_bridge = Singleton(Data_bridge)
        self.gui_root = root

    def main_thread(self):
        self.cap = cv2.VideoCapture(0)
        while self.data_bridge.start_process_manager:
            ret, frame = self.cap.read()
            if ret==True:
                cv2.imshow('Video', frame)
                cv2.waitKey(100)
            else:
                self.data_bridge.start_process_manager = False
                break
            self.gui_root.update()
        cv2.destroyAllWindows()
        self.cap.release()


class Virtual_BG:

    def __init__(self, root):
        self.data_bridge = Singleton(Data_bridge)
        self.gui_root = root
        self.args = self.set_parameters()
        self.get_background = get_segmentation(self.args)

    def set_parameters(self):
        parser = argparse.ArgumentParser(description='Background Matting')
        parser.add_argument('--model',
                            default='C:/Users/Kenil/Desktop/Github/Streamix/data/models/only_par.pth',
                            help='Location of the Trained Model')
        parser.add_argument('--without_gpu', action='store_true', default=True, help='Use CPU')
        parser.add_argument('--background_image',
                            default='C:/Users/Kenil/Desktop/Github/Streamix/data/bg_images/sf_bridge.jpg',
                            help='Location of Background Image')
        parser.add_argument('--input_resolution', default=256, help='Input resolution (Higher == Slower == Acccurate)')
        parser.add_argument('--camera_resolution', default=[640, 360],
                            help='Input resolution (Higher == Slower == Acccurate)')
        parser.add_argument('--camera_id', default=0, help='Camera ID to be used')
        parser.add_argument('--threshold', default=0.75, help='Set Threshold')

        args = vars(parser.parse_args())
        return args

    def main_thread(self):
        self.videoCapture = cv2.VideoCapture(self.args["camera_id"])
        self.videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, self.args["camera_resolution"][0])
        self.videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.args["camera_resolution"][1])
        self.args = self.set_parameters()
        self.args["background_image"] = self.data_bridge.selected_background_file_path
        self.get_background = get_segmentation(self.args)
        while self.data_bridge.start_process_manager:
            ret, frame = self.videoCapture.read()
            if ret==True:
                output = self.get_background.run_torch(frame)
                cv2.imshow('Video', output)
                cv2.waitKey(1)
            else:
                self.data_bridge.start_process_manager = False
                break
            self.gui_root.update()
        cv2.destroyAllWindows()
        self.videoCapture.release()
