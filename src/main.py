from functions.load import load_image


def main():
    load_image(image_name="bill.jpg")
    # image = remove_shadow(image)
    # image = rotate(image)
    # image_textdata = get_dataFrame_text_from_image(image)
    # return image_textdata


if __name__ == "__main__":
    text = main()
    print(text)
