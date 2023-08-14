import PIL
from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedImgs'

for filename in os.listdir(path):
    img=Image.open(f"{path}/{filename}")
    edit= img.filter(ImageFilter.SMOOTH).convert('L')
    factor1= 3.5
    factor2=0.5
    enhancer1= ImageEnhance.Contrast(edit)
    enhancer2= ImageEnhance.Sharpness(edit)
    enhancer3= ImageEnhance.Brightness(edit)
    edit= enhancer1.enhance(factor1)
    edit=enhancer2.enhance(factor1)
    edit=enhancer3.enhance(factor2)
    clean_name=os.path.splitext(filename)[0]
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

