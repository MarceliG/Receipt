import pytesseract
import pandas as pd


def convert_image_to_text(image):
    text = (pytesseract.image_to_string(image)).lower()
    text = text.split("\n")
    text = [sentence.strip() for sentence in text]
    text = [sentence for sentence in text if len(sentence) != 0]
    return text


def get_dataFrame_text_from_image(image):
    text = convert_image_to_text(image)
    data = {"text": text}
    text_data = pd.DataFrame(data=data)

    return text_data
