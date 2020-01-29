import numpy as np 
from numpy import linalg as LA 
from vector import Vector
import math

class Segment:
    angle = 0
    
    def __init__(self, points, len_, i):
        if isinstance(points, list):
            self.a = Vector(points[0], points[1])
            
            self.len = len_
            self.calculateB()
        elif isinstance(points, Segment):
            self.parent = points
            
            a = parent.b.copy()
            len = len_
            calculateB()

    def follow(self, tx, ty):
        if ty == "a":
            targetX = self.child.a.x
            targetY = self.child.a.y
            self.follow(targetX, targetY)
        else:
            target = Vector(tx,ty)
            dirr = target - self.a
            self.angle = dirr.heading()

            dirr.magnitude = self.len
            dirr = dirr * -1
            self.a = target + dirr

    def calculateB(self):
        dx = self.len * math.cos(self.angle)
        dy = self.len * math.sin(self.angle)
        self.b = Vector(self.a.x + dx, self.a.y + dy)

    def update(self):
        self.calculateB()

points = [0,1]
seg = Segment(points, 10,1)