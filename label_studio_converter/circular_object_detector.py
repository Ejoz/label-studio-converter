import os
import json
import numpy as np
from PIL import Image
from collections import defaultdict


tasks = json.load(open("/home/eval/Desktop/label-studio-converter/completions/result.json"))
task = tasks[0]

x = task["tag"][0]["x"]
y = task["tag"][0]["y"]
radiusX = task["tag"][0]["radiusX"]
radiusY = task["tag"][0]["radiusY"]
w = task["tag"][0]["original_width"]
h = task["tag"][0]["original_height"]

import cv2
image = np.zeros((w,h, 3), np.uint8)
image = cv2.ellipse(image, (int(x),int(y)), (int(radiusX), int(radiusY)))
Image.fromarray(image).show()
