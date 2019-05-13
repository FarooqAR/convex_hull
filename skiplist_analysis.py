import random
import time


class Node():
    def __init__(self, key, value, h):
        self.x = (key,value)
        self.next = h*[None] + [None]

class SkipList:

    def __init__(self):
        self.size = 0
        self.sentinel = Node(None, None, 0)
        self.maxh = 0

    def Pick_height(self):
        k = 0
        z = random.getrandbits(32)
        z = str(bin(z))
        z = z[2:]
        for i in z:
            if i == '1':
                k = k + 1
            else:
                break
        return k

    def Add(self, key, value):
        u = self.sentinel
        r = self.maxh 
        stk = self.maxh*[None] + [None]
        while r >= 0:
            while u.next[r] != None and u.next[r].x[0] < key:
                u = u.next[r]
            if u.next[r] != None and u.next[r].x[0] == key:
                return False
            stk[r] = u
            r = r - 1
        temph = self.Pick_height()
        w = Node(key,value,temph)
        while self.maxh < temph:
            self.maxh = self.maxh + 1
            self.sentinel.next.append(None)
            stk.append(self.sentinel)
        for i in range(0,len(w.next)):
            w.next[i] = stk[i].next[i]
            stk[i].next[i] = w
        self.size = self.size + 1

    def Find(self, key):
        u = self.sentinel
        r = self.maxh
        while r >= 0:
            while u.next[r] != None and u.next[r].x[0] < key:
                u = u.next[r]
            r = r- 1
        if u.next[0].x[0] != key:
            return -1
        return u.next[0].x[1]
    
    def GetSize(self):
        return self.size


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def jarvis(sl):
    convex_set = []
    n = sl.GetSize()
    l = 0
    i = 1
    while i < n:
        if sl.Find(i)[0] < sl.Find(l)[0]:
            l = i
        i += 1
    
    p = l
    q = (p + 1) % n
    while True:
        
        j = (q + 1) % n
        found = True
        
        c_a = sl.Find(q)[0] - sl.Find(p)[0]
        d_b = sl.Find(q)[1] - sl.Find(p)[1]
        while j != q:
            e_a = sl.Find(j)[0] - sl.Find(p)[0]
            f_b = sl.Find(j)[1] - sl.Find(p)[1]
            det = f_b * c_a - d_b * e_a # determinant
            
            # we'll take advantage of the fact that the determinant gives us the orientation as well
            if det > 0: # if there is a point j which is left to line p-q
                found = False
            j = (j + 1) % n

        if found:
            convex_set.append(sl.Find(q))
            p = q
            if p == l: # came back to the starting point i.e. loop is complete
                break
        q = (q + 1) % n
    
    return convex_set

sl = SkipList()

def generate_random_points(size):
    count = 0
    for _ in range(size):
        x = random.randint(1,50)
        y = random.randint(1,50)
        sl.Add(count,(x,y))
        count = count + 1

times = []

for i in range(210, 220, 10):
    sl = SkipList()
    generate_random_points(i)
    t1 = time.time()
    jarvis(sl)
    t2 = time.time()
    times.append(t2-t1)

print(times)
print(sum(times)/1)
