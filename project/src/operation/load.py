import os

import cv2
import numpy as np
from config import PHOTOS_DIR
from numpy import typing as npt


def load_image(image_name: str) -> npt.NDArray[np.float_]:
    path = os.path.realpath(os.path.join(PHOTOS_DIR, image_name))
    if os.path.exists(path):
        image: npt.NDArray[np.float_] = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        return image
    else:
        raise Exception("Incorrect path")
