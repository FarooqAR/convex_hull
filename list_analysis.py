# from main import jarvis
import random
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
            convex_set.append(points[q])
            p = q
            if p == l: # came back to the starting point i.e. loop is complete
                break
        q = (q + 1) % n
    
    return convex_set

def generate_random_points(size):
    points = []
    for _ in range(size):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        points.append(Point(x, y))
    return points


times = []

for i in range(350, 360, 10):
    points = generate_random_points(i)
    t1 = time.time()
    jarvis(points)
    t2 = time.time()
    times.append(t2-t1)

print(times)
