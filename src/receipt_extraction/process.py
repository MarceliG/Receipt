import cv2
import matplotlib.pyplot as plt
from skimage.filters import threshold_local


class ImageProcessor:
    def __init__(self):
        pass

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


def image_resize(image, width=None, height=None):
    dim_resize = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the original image
    if width is None and height is None:
        return image

    # if the width is None
    if width is None:
        r = height / float(h)
        dim_resize = (int(w * r), height)
    # if the height is None
    else:
        r = width / float(w)
        dim_resize = (width, int(h * r))

    # resize the image
    resized_image = cv2.resize(image, dim_resize, interpolation=cv2.INTER_AREA)
    return resized_image
