import numpy as np
from PIL import Image, ImageFilter
from numpy.core.fromnumeric import shape
cat = Image.open("day3\cats\cat.jpg")


resized = cat.resize((3000,1000), resample=Image.NEAREST)
# resized.rotate(5).show()
#cat = Image.eval(cat, lambda x:x*x)


cat = cat.filter(ImageFilter.CONTOUR)
cat_numbers = np.array(cat)
a = np.ravel(cat_numbers)
shape = cat_numbers.shape

print(a)
print(shape)

cat_new = Image.fromarray(cat_numbers)
cat_new.show()
