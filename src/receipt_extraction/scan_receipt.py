# import numpy as np
import cv2
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output


def plot_gray(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(image, cmap="Greys_r")


def plot_rgb(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def recognize_text(image):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d["level"])
    boxes = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
    for i in range(n_boxes):
        (x, y, w, h) = (
            d["left"][i],
            d["top"][i],
            d["width"][i],
            d["height"][i],
        )
        boxes = cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # plot_rgb(boxes)
    return boxes


def extract_text(image):
    extracted_text = pytesseract.image_to_string(image)
    # print(extracted_text)
    return extracted_text


if __name__ == "__main__":
    file_name = "/home/marceli/Receipt/project/data/photos/bill.jpg"
    image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    # image = plot_gray(image)
    # image = recognize_text(image)
    texts = extract_text(image)
    print(texts)
