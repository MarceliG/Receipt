import cv2
import numpy as np
from numpy import typing as npt


def remove_shadow(image: npt.NDArray[np.float_]) -> npt.NDArray[np.float_]:
    rgb_planes = cv2.split(image)
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(
            diff_img,
            None,
            alpha=0,
            beta=255,
            norm_type=cv2.NORM_MINMAX,
        )
        result_norm_planes.append(norm_img)
    result_norm: npt.NDArray[np.float_] = cv2.merge(result_norm_planes)
    return result_norm
