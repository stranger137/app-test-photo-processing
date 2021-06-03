
from PIL import Image, ImageEnhance
from PIL.ImageFilter import BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH
import PyQt5
from PIL import Image, ImageDraw, ImageFont


#photo = Image.open("winnie.jpg")
# photo.show()
def write(image, text,coo):
    im = image
    d1 = ImageDraw.Draw(im)
    # Второй параметр шрифта - его размер
    myFont = ImageFont.truetype("times-ro.ttf", 55)
    # Кортеж отвечает за координаты х, у надписи
    d1.text(coo, text, font=myFont)
    return im

def flip(image,coef):
    # Зеркально отражает изображение слева направо
    im = image.transpose(Image.FLIP_LEFT_RIGHT)
    return im

def brightness(image, coefficient):
    # Меняет яркость на соответствующий процент
    enhancer = ImageEnhance.Brightness(image)
    im = enhancer.enhance(coefficient/100)
    return im

def my_filter(image, chosen_filter):
    # Применяет выбранный фильтр к фото

    filters = [BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EMBOSS, FIND_EDGES, SHARPEN, SMOOTH]
    im = image.filter(filters[chosen_filter-1])

    return im

def crop(image, start_x, start_y, finish_x, finish_y):
    # Обрезает фото
    image = image.crop((start_x, start_y, finish_x, finish_y))
    return im

def rotate(image,coef):
    # Поворот изображения
    im = image.rotate(90)
    return im

def contrast(image, coeff):
    # Выбирает контраст изображения (0 - черно-белое, 1 - исходное, значение может расти бесконечно)
    enhancer = ImageEnhance.Contrast(image)
    im = enhancer.enhance(coeff/100)
    return im

def sharpness(image, coeff):
    # Выделяет детали
    enhancer = ImageEnhance.Sharpness(image)
    im = enhancer.enhance(coeff/100)
    return im

def temperature(image, temp):
    # Устанавливает одну из температур на выбор
    # Код взят с https://stackoverflow.com/questions/11884544/setting-color-temperature-for-a-given-image-like-in-photoshop
    kelvin_table = [
     (255,56,0),
     (255,109,0),
     (255,137,18),
     (255,161,72),
     (255,180,107),
     (255,196,137),
     (255,209,163),
     (255,219,186),
     (255,228,206),
     (255,236,224),
     (255,243,239),
     (255,249,253),
     (245,243,255),
     (235,238,255),
     (227,233,255),
     (220,229,255),
     (214,225,255),
     (208,222,255),
     (204,219,255)
    ]

    r, g, b = kelvin_table[temp]
    matrix = ( r / 255.0, 0.0, 0.0, 0.0,
               0.0, g / 255.0, 0.0, 0.0,
               0.0, 0.0, b / 255.0, 0.0 )
    im = image.convert('RGB', matrix)
    return im
