import os

import cv2


def save(path, filename):
    if not os.path.exists(path):
        raise FileNotFoundError
    else:
        cv2.imwrite(path, filename)
