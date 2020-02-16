from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

def White_and_Black(img, the_name):
    img = img.convert("L")
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return

def Rotate(img, degrees, the_name):
    img = img.rotate(degrees)
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return

def Simple_Blur(img, the_name):
    img = img.filter(ImageFilter.BLUR)
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return

def Box_Blur(img, degrees, the_name):
    img = img.filter(ImageFilter.BoxBlur(degrees))
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return

def Gaussian_Blur(img, degrees, the_name):
    img = img.filter(ImageFilter.GaussianBlur(degrees))
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return

def FLIP_LEFT_RIGHT(img, the_name):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return

def FLIP_TOP_BOTTOM(img, the_name):
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return

def add_border(img, border, color, the_name):
    img = ImageOps.expand(img, border = border, fill = color)
    img.save(str(the_name) + "_picture" + ".png")
    img.show()
    return
