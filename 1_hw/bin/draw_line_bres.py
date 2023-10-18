from PIL import Image
import matplotlib.pyplot as plt

def bresenham(x1 : int,y1 : int, x2 : int, y2 : int):
    DIMENSION = 20
    img = Image.new('RGB',(DIMENSION,DIMENSION))
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    step_x = 1 if x2 - x1 >= 0 else -1
    step_y = 1 if y2 - y1 >=0 else -1
    eps = 0
    y = y1
    x = x1
    while (x != x2 + step_x and y != y2 + step_y):
        if (dx == 0):
            while (y != (y2 + step_y)):
                img.putpixel(( x,y),255)
                y += step_y
        if (dy == 0):
            while (x != x2 ):
                print(x)
                img.putpixel(( x,y),255)
                x += step_x
        if (dx != 0):
            if eps >= dx:
                y +=step_y
                eps -= 2 * dx
            print(x,y,eps)
            eps += 2*dy
            img.putpixel(( x,y),255)
            x += step_x
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":

    bresenham(10,7,0,0)