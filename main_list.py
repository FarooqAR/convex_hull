from tkinter import Tk, Canvas, Button, LEFT
import random
import time

random.seed(time.time())
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 500
PAD_X = 50 # use for giving some gap between the points and the window
PAD_Y = 50
POINT_WIDTH = 5

master = Tk() # root widget
points = [] # instances of Point class
lines = [] # we'll save line widgets so we can remove them later
# create canvas
canvas = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack() # render canvas

class Point:
    def __init__(self, canvas_ref, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.__drawn__= None
        self.__canvas__ = canvas_ref
        self.__deleted__ = True

    def draw(self):
        self.__drawn__ = self.__canvas__.create_oval(self.x, self.y, self.x, self.y, width=self.width)
        self.__deleted__ = False

    def mark(self):
        self.__canvas__.itemconfig(self.__drawn__, outline="red")
    
    def delete(self):
        self.__canvas__.delete(self.__drawn__)
        self.__deleted__ = True

def generate_random_points(size):
    points = []
    for _ in range(size):
        x = random.randint(PAD_X, CANVAS_WIDTH - PAD_X)
        y = random.randint(PAD_Y, CANVAS_HEIGHT - PAD_Y)
        points.append(Point(canvas, x, y, POINT_WIDTH))
    return points

def draw_points(points):
    for point in points:
        point.draw()

def clear_points(points):
    for point in points:
        point.delete()

def clear_lines(lines):
    for line in lines:
        canvas.delete(line)

def redraw_points():
    global points
    global lines
    clear_points(points)
    clear_lines(lines)
    points = generate_random_points(2000)
    draw_points(points)

def jarvis(points):
    n = len(points)
    if n == 0:
        return points

    convex_set = []
    l = 0
    i = 1
    while i < n:
        if points[i].x < points[l].x:
            l = i
        i += 1
    
    p = l
    points[p].mark()
    q = (p + 1) % n
    while True:
        
        j = (q + 1) % n
        found = True
        c_a = points[q].x - points[p].x
        d_b = points[q].y - points[p].y
        while j != q:
            e_a = points[j].x - points[p].x
            f_b = points[j].y - points[p].y
            det = f_b * c_a - d_b * e_a # determinant
            
            # we'll take advantage of the fact that the determinant gives us the orientation as well
            if det > 0: # if there is a point j which is left to line p-q
                found = False
            j = (j + 1) % n

        if found:
            points[q].mark()
            convex_set.append(points[q])
            p = q
            if p == l: # came back to the starting point i.e. loop is complete
                break
        q = (q + 1) % n
    
    return convex_set

def draw_convex(points):
    n = len(points)
    for i in range(n):
        if i < n - 1:
            line = canvas.create_line(points[i].x, points[i].y, points[i + 1].x, points[i + 1].y)
            lines.append(line)
        else:
            line = canvas.create_line(points[i].x, points[i].y, points[0].x, points[0].y)
            lines.append(line)
            

# initialize buttons
btn_gen_points = Button(master, text="Generate Points", command=redraw_points)
btn_run_algo = Button(master, text="Run Algo", command=lambda: draw_convex(jarvis(points)))

# render the buttons
btn_gen_points.pack(side=LEFT)
btn_run_algo.pack(side=LEFT)

master.mainloop()