from PIL import Image

def White_and_Black(img, the_name, weight, height):
    mig = 100
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            khahk = (r + g + b) // 3
            if khahk > mig:
                img.putpixel((x, y), (255, 255, 255))
            else:
                img.putpixel((x, y), (0, 0, 0))
    img.save(str(the_name) + ".jpg")
    img = Image.open('picture.jpg')
    return

def Mirroring(img, the_name, weight, height):
    img_pixels = []
    for x in range(weight):
        l = []
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            l.append((r, g, b))
        img_pixels.append(l)
    bank = 0
    z = weight - 1
    for x in range(weight):
        l = img_pixels[z]
        bank = 0
        for y in range(height):
            r, g, b = l[bank]
            img.putpixel((x, y), (r, g, b))
            if bank < len(l) - 1:
                bank += 1
        z -= 1
    img.save(str(the_name) + ".jpg")
    img = Image.open('picture.jpg')
    return

def Checkered(img, the_name, weight, height):
    for x in range(weight):
        for y in range(height):
            mig = [0, 0, 0]
            zakh = [[x, y], [x - 1, y], [x + 1, y],[x, y - 1],[x, y + 1],[x - 1, y -1],[x - 1, y + 1],[x + 1, y - 1],[x + 1, y - 1]]
            for i in range(9):
                if zakh[i][0] != -1 and zakh[i][0] != weight and zakh[i][1] != -1 and zakh[i][1] != height:
                    r, g, b = img.getpixel((zakh[i][0], zakh[i][1]))
                    mig[0] += r
                    mig[1] += g
                    mig[2] += b
            for i in range(9):
                if zakh[i][0] != -1 and zakh[i][0] != weight and zakh[i][1] != -1 and zakh[i][1] != height:
                    img.putpixel((zakh[i][0], zakh[i][1]), (mig[0] // 9, mig[1] // 9, mig[2] // 9))
    img.save(str(the_name) + ".jpg")
    img = Image.open('picture.jpg')
    return

def Blur_the_image(img, the_name, weight, height):
    for x in range(weight):
        for y in range(height):
            mig = [0, 0, 0]
            h = 0
            zakh = [[x - 1, y], [x + 1, y],[x, y - 1],[x, y + 1],[x - 1, y -1],[x - 1, y + 1],[x + 1, y - 1],[x + 1, y - 1]]
            for i in range(8):
                if zakh[i][0] != -1 and zakh[i][0] != weight and zakh[i][1] != -1 and zakh[i][1] != height:
                    r, g, b = img.getpixel((zakh[i][0], zakh[i][1]))
                    mig[0] += r
                    mig[1] += g
                    mig[2] += b
            img.putpixel((x, y), (mig[0] // 8, mig[1] // 8, mig[2] // 8))
    img.save(str(the_name) + ".jpg")
    img = Image.open('picture.jpg')
    return






































