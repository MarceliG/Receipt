import cv2
from detector import ReceiptDetector
from process import ImageProcessor
import os


def extract_receipt(image_path):
    image_processor = ImageProcessor()
    receipt_detector = ReceiptDetector()

    image = cv2.imread(image_path)

    resize_ratio = 500 / image.shape[0]
    original = image.copy()
    image = image_processor.opencv_resize(image, resize_ratio)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get rid of noise with Gaussian Blur filter
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    dilated = cv2.dilate(blurred, rectKernel)

    # Detect white regions
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    edged = cv2.Canny(dilated, 100, 200, apertureSize=3)

    # Detect all contours in Canny-edged image
    contours, hierarchy = cv2.findContours(
        edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )
    largest_contours = sorted(contours, key=cv2.contourArea, reverse=True)
    receipt_contour = receipt_detector.get_receipt_contour(largest_contours)

    scanned = receipt_detector.wrap_perspective(
        original.copy(),
        receipt_detector.contour_to_rect(receipt_contour, resize_ratio),
    )

    # Convert from BGR to RGB
    scanned_rgb = cv2.cvtColor(scanned, cv2.COLOR_BGR2RGB)

    # Saving the image
    save_path = os.path.join(RECEIPT_DIR, "receipt.png")
    print(save_path)
    cv2.imwrite(save_path, scanned_rgb)

    # (x, y, w, h) = cv2.boundingRect(largest_contours[0])

    # # to demonstrate the impact of contour approximation, let's loop
    # # over a number of epsilon sizes
    # peri = cv2.arcLength(largest_contours[0], True)

    # for eps in np.linspace(0.001, 0.05, 10):
    #     # approximate the contour
    #     approx = cv2.approxPolyDP(largest_contours[0], eps * peri, True)
    #     # draw the approximated contour on the image
    #     output = image.copy()
    #     cv2.drawContours(output, [approx], -1, (0, 255, 0), 3)
    #     text = "eps={:.4f}, num_pts={}".format(eps, len(approx))
    #     cv2.putText(output, text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    #     # show the approximated contour image
    #     print("[INFO] {}".format(text))
    #     if len(approx) <= 4:
    #         break
    # plt.imshow(output)
