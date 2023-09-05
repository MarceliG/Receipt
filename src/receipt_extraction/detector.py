import cv2
import numpy as np


class ReceiptDetector:
    def __init__(self):
        pass

    def approximate_contour(self, contour):
        peri = cv2.arcLength(contour, True)
        return cv2.approxPolyDP(contour, 0.02 * peri, True)

    def get_receipt_contour(self, contours):
        for c in contours:
            approx = self.approximate_contour(c)
            return approx

    def contour_to_rect(self, contour, resize_ratio):
        pts = contour.reshape(4, 2)
        rect = np.zeros((4, 2), dtype="float32")
        # top-left point has the smallest sum
        # bottom-right has the largest sum
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        # compute the difference between the points:
        # the top-right will have the minumum difference
        # the bottom-left will have the maximum difference
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect / resize_ratio

    def wrap_perspective(self, img, rect):
        # unpack rectangle points:
        # top left, top right, bottom right, bottom left
        (tl, tr, br, bl) = rect
        # compute the width of the new image
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        # compute the height of the new image
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        # take the maximum of the width and height values to reach
        # our final dimensions
        maxWidth = max(int(widthA), int(widthB))
        maxHeight = max(int(heightA), int(heightB))
        # destination points which will be used to map
        # the screen to a "scanned" view
        dst = np.array(
            [
                [0, 0],
                [maxWidth - 1, 0],
                [maxWidth - 1, maxHeight - 1],
                [0, maxHeight - 1],
            ],
            dtype="float32",
        )
        # calculate the perspective transform matrix
        M = cv2.getPerspectiveTransform(rect, dst)
        # warp the perspective to grab the screen
        return cv2.warpPerspective(img, M, (maxWidth, maxHeight))
