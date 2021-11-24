import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from numpy.core.fromnumeric import shape


cat = Image.open("day3\cats\cat.jpg")
draw = ImageDraw.Draw(cat)  # Создаем инструмент для рисования
width = cat.size[0]  # Определяем ширину
height = cat.size[1]  # Определяем высоту
pix = cat.load()  # Выгружаем значения пикселей


# Инверсия получается путём вычета из 255 текущего цвета:

for x in range(width):
   for y in range(height):
      r = pix[x, y][0]
      g = pix[x, y][1]
      b = pix[x, y][2]
      draw.point((x, y), (255 - r, 255 - g, 255 - b))

cat.show()