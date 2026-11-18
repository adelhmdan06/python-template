from PIL import Image


def decode_terrorist_message(image_path):
    img = Image.open(image_path)

    img = img.convert('RGB')
    width, height = img.size
    message = ""
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if r == 0 and g == 0 and b == 0:
                message += chr(y)
                break
    return message

secret_message = decode_terrorist_message('code.png')
print("המסר שפוענח הוא:")
print(secret_message)