import os

from PIL import Image as img


def circleBres(xc,yc,r)  :
    im = img.new(mode='1', size=(13,13),color=1)
    x,y = 0,r
    d = 3 - 2 * r
    drawCircle(xc, yc, x, y,im)
    print(x,y,d)
    while (y >= x):

        x+=1
        if (d > 0):
            y-=1
            d = d + 4 * (x - y) + 10

        else:
            d = d + 4 * x + 6
        print(x, y, d)

        drawCircle(xc, yc, x, y,im)
    print(im)
    im.show()

def drawCircle(xc, yc ,x, y,im):

    im.putpixel((xc+x, yc+y), 0)
    im.putpixel((xc-x, yc+y), 0)
    im.putpixel((xc+x, yc-y), 0)
    im.putpixel((xc-x, yc-y), 0)
    im.putpixel((xc+y, yc+x), 0)
    im.putpixel((xc-y, yc+x), 0)
    im.putpixel((xc+y, yc-x), 0)
    im.putpixel((xc-y, yc-x), 0)


if __name__ == "__main__":

    circleBres(0, 0 , 6)