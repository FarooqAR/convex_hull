#!/bin/python3

import math
import os
import random
import re
import sys
from enum import Enum

from tkinter import Tk, Canvas, Button, LEFT
import time


class Node():
    def __init__(self, key, value, h):
        self.x = (key,value)
        self.next = h*[None] + [None]



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



sl = SkipList() # object of skip List

def generate_random_points():
    points = []
    count = 1
    for _ in range(30):
        x = random.randint(1,50)
        y = random.randint(1,50)
        sl.Add(count,(x,y))
        count = count + 1


generate_random_points()



print(sl.GetSize())

print(sl.Find(4)[0]) # This is a sample to show you that through this function we can accses the 'x' value at index 4. The index is starting from 1.


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
    sl.Find(p).mark()
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
            sl.Find(q).mark()
            convex_set.append(sl.Find(q))
            p = q
            if p == l: # came back to the starting point i.e. loop is complete
                break
        q = (q + 1) % n
    
    return convex_set




