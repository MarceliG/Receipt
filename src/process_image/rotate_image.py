"""Automatically detect rotation and line spacing of an image of text using."""

import imutils
import numpy as np
from numpy import argmax, array
from numpy import typing as npt
from skimage.transform import radon


def calculate_rms(x_seq: npt.NDArray[np.float_]) -> float:
    sum_of_squares = 0
    for x in x_seq:
        sum_of_squares += x * x

    mean_of_squares = sum_of_squares / len(x_seq)
    rms: float = mean_of_squares ** (1 / 2)
    return rms


def detect_angle(image: npt.NDArray[np.float_]) -> float:
    # Do the radon transform and display the result
    sinogram = radon(image)
    # Find the RMS value of each row and find "busiest" rotation,
    # where the transform is lined up perfectly with the alternating dark
    # text and white lines
    r = array([calculate_rms(line) for line in sinogram.transpose()])
    angle: float = float(argmax(r))
    # angle = argmax(r) -90
    return angle


def rotate(image: npt.NDArray[np.float_]) -> npt.NDArray[np.float_]:
    angle = detect_angle(image)
    rotate_image: npt.NDArray[np.float_] = imutils.rotate_bound(image, angle)
    return rotate_image
