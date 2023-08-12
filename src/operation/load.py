import os

import cv2

# import numpy as np
from utils import PHOTOS_DIR

# from numpy import typing as npt


# def load_image(image_name: str) -> npt.NDArray[np.float_]:
#     path = os.path.realpath(os.path.join(PHOTOS_DIR, image_name))
#     if os.path.exists(path):
#         image: npt.NDArray[np.float_] = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#         return image
#     else:
#         raise Exception("Incorrect path")


# TODO chanege to load orginal image and second function loaad resize image
def load_image(
    image_name: str,
    dimension_resize: int = 800,
    interpolation: int = cv2.INTER_LANCZOS4,
):
    path = os.path.realpath(os.path.join(PHOTOS_DIR, image_name))
    if os.path.exists(path):
        image = cv2.imread(path)
        height, width = image.shape[:2]

        if height > width:
            new_height = dimension_resize
            new_width = int(width * (dimension_resize / height))
        else:
            new_width = dimension_resize
            new_height = int(height * (dimension_resize / width))

        # Zeskaluj obraz
        resized_image = cv2.resize(
            image,
            (new_width, new_height),
            interpolation=interpolation,
        )
        return resized_image
    else:
        raise Exception("Incorrect path")
