from tkinter import *


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

MAX_ITERATIONS = 200


X1 = -2
X2 = 1.0

Y1 = -1.2
Y2 = Y1 + (X2 - X1) * SCREEN_HEIGHT / SCREEN_WIDTH


def drawPoint(x, y, canvas, color):
    canvas.create_line(x, y, x + 1, y, fill=color)



def getIterations(c, maxIterations):
    counter = 0
    z = 0

    while True:
        #Zn+1 = Zn² + c
        z = z * z + c
        counter += 1
        if counter >= maxIterations or abs(z) > 2:
            return counter


def getColor(iterations):
    if 255 - iterations * 15 < 10:
        return 'white'
    color = (255 - iterations * 15, 0, 0)
    color = '#%02x%02x%02x' % color

    return color





root = Tk()
c = Canvas(root, bg='white', width=SCREEN_WIDTH, height=SCREEN_HEIGHT, name="canvas")
c.pack()

dx = (X2 - X1) / (SCREEN_WIDTH-1)
dy = (Y2 - Y1) / (SCREEN_HEIGHT-1)

# loop every pixel
for x in range(SCREEN_WIDTH - 1):
    re = X1 + x * dx

    for y in range(SCREEN_HEIGHT - 1):
        im = Y2 - y * dy
        iterations = getIterations(complex(re, im), MAX_ITERATIONS)
        if iterations >= MAX_ITERATIONS:
            drawPoint(x, y, c, 'black')
        else:
            drawPoint(x, y, c, getColor(iterations))


root.mainloop()