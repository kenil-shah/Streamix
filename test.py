import unittest
import torch
import cv2
import flask
import numpy
import sys
sys.path.insert(1, 'code')
from python_background_pipeline.net.segnet import SegMattingNet
from python_background_pipeline.segmenter import get_segmentation


class TestStreamix(unittest.TestCase):
    def test_bg_image(self):
        img = cv2.imread("data/bg_images/HomeBG.jpg")

    def test_model_loading(self):
        model = "data/models/only_params.pth"
        self.myModel = SegMattingNet()
        self.myModel.load_state_dict(torch.load(model), strict=False)
        self.myModel.eval()
        self.myModel.to(torch.device('cpu'))

    def test_model_working(self):
        self.test_model_loading()
        img = cv2.imread("data/bg_images/HomeBG.jpg")
        image_resize = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
        tensor_4D = torch.FloatTensor(1, 3, 256, 256)
        tensor_4D[0, :, :, :] = torch.FloatTensor(image_resize.transpose(2, 0, 1))
        inputs = tensor_4D.to(torch.device('cpu'))
        seg, alpha = self.myModel(inputs)


if __name__ == '__main__':
    main = TestStreamix()
    import sys
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStreamix)
    unittest.TextTestRunner(verbosity=4, stream=sys.stderr).run(suite)
