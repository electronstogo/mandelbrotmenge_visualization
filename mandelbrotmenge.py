# 2018 - electronstogo

from tkinter import *


# Size constants of picture.
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

# Max iterations for color calculations. Defines the resolution of the picture.
# As more iterations are defined, as long the calculations will take.
MAX_ITERATIONS = 200


# coordinates for the coordinate system.
# needed for calculation of real and imaginary part.
X1 = -2
X2 = 1.0

Y1 = -1.2
# mapping of coordinate system value to the image pixels.
Y2 = Y1 + (X2 - X1) * SCREEN_HEIGHT / SCREEN_WIDTH




class Mandelbrotmenge:
    def __init__(self):
        self.root = Tk()
        self.root.title('Mandelbrotmenge')
        self.canvas = Canvas(self.root, bg='white', width=SCREEN_WIDTH, height=SCREEN_HEIGHT, name="canvas")
        self.canvas.pack()

        self.dx = (X2 - X1) / (SCREEN_WIDTH - 1)
        self.dy = (Y2 - Y1) / (SCREEN_HEIGHT - 1)

        self.do_calculations()

        self.root.mainloop()



    def do_calculations(self):
        # loop every pixel
        for pos_x in range(SCREEN_WIDTH - 1):
            re = X1 + pos_x * self.dx

            for pos_y in range(SCREEN_HEIGHT - 1):
                im = Y2 - pos_y * self.dy
                iterations = self.get_iterations(complex(re, im), MAX_ITERATIONS)
                if iterations >= MAX_ITERATIONS:
                    self.draw_point(pos_x, pos_y, 'black')
                else:
                    self.draw_point(pos_x, pos_y, self.get_color(iterations))


    def draw_point(self, pos_x, pos_y, color):
        self.canvas.create_line(pos_x, pos_y, pos_x + 1, pos_y, fill=color)


    # calculate the iterations needed.
    @staticmethod
    def get_iterations(c, max_iterations):
        iteration_counter = 0
        z = 0

        while True:
            # Zn+1 = Zn² + c
            z = z * z + c
            iteration_counter += 1

            if iteration_counter >= max_iterations or abs(z) > 2:
                return iteration_counter


    # get color calculated from iterations
    @staticmethod
    def get_color(iterations):
        if 255 - iterations * 15 < 10:
            return 'white'

        color = (255 - iterations * 15, 0, 0)
        color = '#%02x%02x%02x' % color

        return color




if __name__ == '__main__':
    Mandelbrotmenge()
