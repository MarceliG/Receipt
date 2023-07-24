import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_local
import os
from const import PHOTOS_DIR


class ImageProcessor:
    def __init__(self):
        pass

    def load_image(
        self,
        image_name,
        dimension_resize=800,
        interpolation=cv2.INTER_LANCZOS4,
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

            resized_image = cv2.resize(
                image,
                (new_width, new_height),
                interpolation=interpolation,
            )
            return resized_image
        else:
            raise Exception("Incorrect path")

    def opencv_resize(self, image, ratio):
        width = int(image.shape[1] * ratio)
        height = int(image.shape[0] * ratio)
        dim = (width, height)
        return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    def plot_rgb(self, image):
        plt.figure(figsize=(16, 10))
        return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    def plot_gray(self, image):
        plt.figure(figsize=(16, 10))
        return plt.imshow(image, cmap="Greys_r")

    def bw_scanner(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        T = threshold_local(gray, 21, offset=5, method="gaussian")
        return (gray > T).astype("uint8") * 255
