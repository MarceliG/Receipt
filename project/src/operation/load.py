import os
import cv2

from config import PHOTOS_DIR


def load_image(image_name: str):
    path = os.path.realpath(os.path.join(PHOTOS_DIR, image_name))
    if os.path.exists(path):
        # return cv2.imread(path, cv2.COLOR_BGR2GRAY)
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        # return cv2.imread(path)
    else:
        raise Exception("Incorrect path")
