# Жмем любые изображения для сайта "дом питомца"
from PIL import Image
import glob

types = ('*.png', '*.jpg')
files_grabbed = []


def img_compress():
    for files in types:
        files_grabbed.extend(glob.glob(files))
    for i in files_grabbed:
        img = Image.open(i)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(f'output/{i}')

img_compress()