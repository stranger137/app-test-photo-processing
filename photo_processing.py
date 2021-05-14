from PIL import Image, ImageEnhance
from PIL.ImageFilter import BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH
import PyQt5

photo = Image.open("winnie.jpg")
# photo.show()

def flip(image):
    # Зеркально отражает изображение слева направо
    im = image.transpose(Image.FLIP_LEFT_RIGHT)
    return im

def brightness(image, coefficient):
    # Меняет яркость на соответствующий процент
    im = image.point(lambda i: i * coefficient)
    return im

def filter(image, chosen_filter):
    # Применяет выбранный фильтр к фото
    im = image.filter(chosen_filter)
    return im

def crop(image, start_x, start_y, finish_x, finish_y):
    # Обрезает фото
    im = image.crop((start_x, start_y, finish_x, finish_y))
    return im

def rotate(image, degree):
    # Поворот изображения
    im = image.rotate(degree)
    return im

def contrast(image, coeff):
    # Выбирает контраст изображения (0 - черно-белое, 1 - исходное, значение может расти бесконечно)
    enhancer = ImageEnhance.Contrast(image)
    im = enhancer.enhance(coeff)
    return im

def sharpness(image, coeff):
    # Выделяет детали
    enhancer = ImageEnhance.Sharpness(image)
    im = enhancer.enhance(coeff)
    return im

def temperature(image, temp):
    # Устанавливает одну из температур на выбор
    kelvin_table = {
    1000: (255,56,0),
    1500: (255,109,0),
    2000: (255,137,18),
    2500: (255,161,72),
    3000: (255,180,107),
    3500: (255,196,137),
    4000: (255,209,163),
    4500: (255,219,186),
    5000: (255,228,206),
    5500: (255,236,224),
    6000: (255,243,239),
    6500: (255,249,253),
    7000: (245,243,255),
    7500: (235,238,255),
    8000: (227,233,255),
    8500: (220,229,255),
    9000: (214,225,255),
    9500: (208,222,255),
    10000: (204,219,255)
    }

    r, g, b = kelvin_table[temp]
    matrix = ( r / 255.0, 0.0, 0.0, 0.0,
               0.0, g / 255.0, 0.0, 0.0,
               0.0, 0.0, b / 255.0, 0.0 )
    im = image.convert('RGB', matrix)
    return im
