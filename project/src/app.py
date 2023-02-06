from operation import load_image
from process_image import remove_shadow, rotate, get_dataFrame_text_from_image


def main():
    image = load_image(image_name="bill.jpg")
    image1 = remove_shadow(image=image)
    image2 = rotate(image=image1)
    image_textdata = get_dataFrame_text_from_image(image=image2)
    return image_textdata


if __name__ == "__main__":
    text = main()
    print(text)
