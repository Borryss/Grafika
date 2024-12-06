from PIL import Image
import numpy as np
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt

im = Image.open("baby_yoda.jpg")
im_copy = im

im.show()
im_copy.filter(ImageFilter.FIND_EDGES).show()

def filtruj(obraz, kernel, scale):
    print("asd")


