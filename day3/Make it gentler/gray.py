import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from numpy.core.fromnumeric import shape


cat = Image.open("day3\cats\cat.jpg")
draw = ImageDraw.Draw(cat)  # Создаем инструмент для рисования
width = cat.size[0]  # Определяем ширину
height = cat.size[1]  # Определяем высоту
pix = cat.load()  # Выгружаем значения пикселей

for x in range(width):
    for y in range(height):
       r = pix[x, y][0] #узнаём значение красного цвета пикселя
       g = pix[x, y][1] #зелёного
       b = pix[x, y][2] #синего
       sr = (r + g + b) // 3 #среднее значение для серого пикспеля
       draw.point((x, y), (sr, sr, sr)) #рисуем пиксель

cat.show()