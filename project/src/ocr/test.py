import sys
import os

try:
    current = os.path.dirname(os.path.realpath(__file__))
    parent = os.path.dirname(current)
    sys.path.append(parent)
except NameError as error:
    raise error

from operation.load import load_image

load_image("zdj.jpg")
