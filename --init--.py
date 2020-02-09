#school project
#amirali yazdiani & ali habibi
from PIL import Image
from effects import *

####geting the picture
the_name_of_picture = input("what is the name of your picture? \n")
img = Image.open(the_name_of_picture + '.png')

weight = img.size[0]
height = img.size[1]

num_change = 1

######what can i do
what_can_i_do = "hi i am the program written by amirali & ali. i can change the pictures that you want. i can: \n 1.White and black \n 2.Rotate \n 3.Simple Blur \n 4.Box Blur \n 5.Gaussian_Blur \n 6.FLIP_LEFT_RIGHT \n 7. FLIP_TOP_BOTTOM \n"
print(what_can_i_do)

######running the program
while(True):

    fir_com = int(input())

    if fir_com == 1:
        White_and_Black(img, num_change)
        img = Image.open(the_name_of_picture + '.png')
        num_change += 1

    elif fir_com == 2:
        degrees = int(input("how many degrees do you want to rotate? \n"))
        Rotate(img, degrees, num_change)
        img = Image.open(the_name_of_picture + '.png')
        num_change += 1

    elif fir_com == 3:
        Simple_Blur(img, num_change)
        img = Image.open(the_name_of_picture + '.png')
        num_change += 1

    elif fir_com == 4:
        degrees = int(input("the amount of blur \n"))
        Box_Blur(img, degrees, num_change)
        img = Image.open(the_name_of_picture + '.png')
        num_change += 1

    elif fir_com == 5:
        degrees = int(input("the amount of blur \n"))
        Gaussian_Blur(img, degrees, num_change)
        img = Image.open(the_name_of_picture + '.png')
        num_change += 1

    elif fir_com == 6:
        FLIP_LEFT_RIGHT(img, num_change)
        img = Image.open(the_name_of_picture + '.png')
        num_change += 1

    elif fir_com == 7:
        FLIP_TOP_BOTTOM(img, num_change)
        img = Image.open(the_name_of_picture + '.png')
        num_change += 1
