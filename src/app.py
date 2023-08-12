from operation import load_image
from process_image import get_dataFrame_text_from_image, remove_shadow, rotate


def main():
    image = load_image(image_name="bill.jpg")
    image = remove_shadow(image)
    image = rotate(image)
    image_textdata = get_dataFrame_text_from_image(image)
    return image_textdata


if __name__ == "__main__":
    text = main()
    print(text)
