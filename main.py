import numpy as np 
from numpy import linalg as LA 
def ditance_from_target(a, b):
    return LA.norm(a-b)
def partialGradient(target, angles, i):
    angle = angles[i]
    # Gradient : [F(x+SamplingDistance) - F(x)] / h
    f_x = DistanceFromTarget(target, angels)
def InverseKinematics(target, angles):
    for i in Joints:
        gradient = partialGradient(target, angles, i)
        angles[i] -= LR *gradient
a = np.array([1,2,3])
b = np.array([4,5,6])
print(dist)