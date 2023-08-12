import numpy as np
import pandas as pd
import pytesseract
from numpy import typing as npt


def convert_image_to_text(image: npt.NDArray[np.float_]) -> list[str]:
    text = (pytesseract.image_to_string(image)).lower()
    text = text.split("\n")
    text = [sentence.strip() for sentence in text]
    all_text = [sentence for sentence in text if len(sentence) != 0]
    return all_text


def get_dataFrame_text_from_image(
    image: npt.NDArray[np.float_],
) -> pd.DataFrame:
    text = convert_image_to_text(image)
    data = {"text": text}
    text_data: pd.DataFrame = pd.DataFrame(data)
    return text_data
