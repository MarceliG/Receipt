
import cv2


def save(path, image):
    # if not os.path.exists(path):
    #     raise FileNotFoundError
    # else:
    cv2.imwrite(path, image)
