#school project
#amirali yazdiani & ali habibi
from PIL import Image
from effects import *

####geting the picture
img = Image.open(input("what is the name of your picture? \n") + '.jpg')
main_img = img

weight = img.size[0]
height = img.size[1]

name = "picture_"
num_change = 1

######what can i do
what_can_i_do = "hi i am the program written by amirali & ali. i can change the pictures that you want. i can: \n 1.White and black \n 2.Mirroring \n 3.Checkered \n 4.Blur the image \n "
print(what_can_i_do)

######running the program
while(True):
    
    fir_com = int(input())
    
    if fir_com == 1:
        White_and_Black(img, num_change, weight, height)
        img = main_img
        num_change += 1

    elif fir_com == 2:
        Mirroring(img, num_change, weight, height)
        img = main_img
        num_change += 1

    elif fir_com == 3:
        Checkered(img, num_change, weight, height)
        img = main_img
        num_change += 1

    elif fir_com == 4:
        Blur_the_image(img, num_change, weight, height)
        img = main_img
        num_change += 1
        
