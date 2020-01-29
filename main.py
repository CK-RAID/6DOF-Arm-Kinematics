import numpy as np 
from numpy import linalg as LA 
import vector

class Segment:
    def __init__(self, point, length, i):
        self.par = point
        self.a = self.par.copy()

        self.b = Vector(0,0)
        self.angle = 0
        self.sw = remap(i, (0, 20), (1, 10))
        self.len = length
        self.calculateB()

    def follow(tx, ty):
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

    def calculateB():
        dx = self.len * math.cos(self.angle)
        dy = self.len * math.sin(self.angle)
        self.b = Vector(self.a.x + dx, self.a.y + dy)

    def update():
        self.calculateB()



seg = Segment(2,3,4)