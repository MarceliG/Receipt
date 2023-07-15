import os
import sys

try:
    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    sys.path.append(parent)
except NameError as error:
    raise error


import numpy as np
import cv2
import matplotlib.pyplot as plt

from skimage.filters import threshold_local
from PIL import Image
from operation.load import load_image


def opencv_resize(image, ratio):
    width = int(image.shape[1] * ratio)
    height = int(image.shape[0] * ratio)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def plot_rgb(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def plot_gray(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(image, cmap="Greys_r")


def downscale_image(image: np.ndarray, resize_ratio: int = 500):
    """Downscale image as finding receipt contour is more efficient
    on a small image."""

    resize = resize_ratio / image.shape[0]
    image = opencv_resize(image, resize)
    return image

    # # Convert to grayscale for further processing
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # plot_gray(gray)


if __name__ == "__main__":
    file_name = "/home/marceli/Receipt/project/data/photos/curve_2.jpg"
    image = cv2.imread(file_name)

    # Get rid of noise with Gaussian Blur filter
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    plot_gray(blurred)

    # Detect white regions
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    dilated = cv2.dilate(blurred, rectKernel)
    plot_gray(dilated)

    # plot only edges detected regions
    edged = cv2.Canny(dilated, 100, 200, apertureSize=3)
    plot_gray(edged)

    # Detect all contours in Canny-edged image
    contours, hierarchy = cv2.findContours(
        edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    image_with_contours = cv2.drawContours(
        image.copy(), contours, -1, (0, 255, 0), 3
    )
    plot_rgb(image_with_contours)

    largest_contours = sorted(contours, key=cv2.contourArea, reverse=True)
    image_with_largest_contours = cv2.drawContours(
        image.copy(), largest_contours, -1, (0, 255, 0), 3
    )
    plot_rgb(image_with_largest_contours)
