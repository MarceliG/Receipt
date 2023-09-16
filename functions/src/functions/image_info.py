import numpy as np


def image_dimensions(image: np.ndarray) -> tuple:
    """Calculate height, width and number of channels from images.

    Args:
        image (np.ndarray): image

    Returns:
        dimension (tuple): height, width, number of channels
    """
    h, w, c = image.shape[:3]
    dimension = (h, w, c)
    return dimension
