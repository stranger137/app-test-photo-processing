from PIL import Image
import PyQt5

photo = Image.open("winnie.jpg")
# photo.show()

def flip(image):
    # Зеркально отражает изображение слева направо
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return image

def change_brightness(image, coefficient):
    image = image.point(lambda i: i * coefficient)
    return image

photo = change_brightness(photo,0.2)
photo.show()





