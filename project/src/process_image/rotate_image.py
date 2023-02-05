"""Automatically detect rotation and line spacing of an image of text using."""

from skimage.transform import radon
from numpy import array, argmax
import imutils


def detect_angle(image):
    # Do the radon transform and display the result
    sinogram = radon(image)
    # Find the RMS value of each row and find "busiest" rotation,
    # where the transform is lined up perfectly with the alternating dark
    # text and white lines
    rms = lambda x_seq: (sum(x * x for x in x_seq) / len(x_seq)) ** (1 / 2)
    r = array([rms(line) for line in sinogram.transpose()])
    angle = argmax(r) - 90
    return angle


def rotate(image):
    angle = detect_angle(image)
    rotate_image = imutils.rotate_bound(image, angle)
    return rotate_image
