# from main import jarvis
import random
import time


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.length = 0

    def insert_at_start(self,x, y):
        if self.start_node is None:
            new_node = Point(x, y)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Point(x, y)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node
        print("yas")


    def insert_at_end(self, x, y):
        self.length+=1
        if self.start_node is None:
            new_node = Point(x, y)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Point(x, y)
        n.nref = new_node
        new_node.pref = n




    def traverse_list(self, i):
        c = 0
        #print("bro")
        if self.start_node is None:
            print("List has no element")
            return
        
        else:
            
            n = self.start_node
            while n is not None:
                if c == i:
                    return n
                #print(n.x , "\n")
                n = n.nref
                c+=1
                
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nref = None
        self.pref = None

points = DoublyLinkedList()

def jarvis():
    if points.length == 0:
        return points

    convex_set = []
    l = 0
    i = 1
    while i < points.length:
        if (points.traverse_list(i)).x < (points.traverse_list(l)).x:
            l = i
        i += 1
    
    p = l
    q = (p + 1) % points.length
    while True:
        
        j = (q + 1) % points.length
        found = True
        c_a = (points.traverse_list(q)).x - (points.traverse_list(p)).x
        d_b = (points.traverse_list(q)).y - (points.traverse_list(p)).y
        while j != q:
            e_a = (points.traverse_list(j)).x - (points.traverse_list(p)).x
            f_b = (points.traverse_list(j)).y - (points.traverse_list(p)).y
            det = f_b * c_a - d_b * e_a # determinant
            
            # we'll take advantage of the fact that the determinant gives us the orientation as well
            if det > 0: # if there is a point j which is left to line p-q
                found = False
            j = (j + 1) % points.length

        if found:
            convex_set.append((points.traverse_list(q)))
            p = q
            if p == l: # came back to the starting point i.e. loop is complete
                break
        q = (q + 1) % points.length
    
    return convex_set

def generate_random_points(size):
    for _ in range(size):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        points.insert_at_end(x, y)
    return points

times = []

for i in range(240, 380, 10):
    points = DoublyLinkedList()
    generate_random_points(i)
    t1 = time.time()
    jarvis()
    t2 = time.time()
    times.append(t2-t1)

print(times)
