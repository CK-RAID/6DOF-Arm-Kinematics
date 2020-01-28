import numpy as np
import math

SamplingDistance = 0
LR = 0.01
DistanceThresh = 1
def DistanceFromTarget(target, angles):
    point = ForwardKinematics(angles)
    return Distance(point, target)

def PartialGradient(target, angles, i):
    global SamplingDistance
    angles = angles[i]
    # Gradient : [F(x+SamplingDistance) - F(x)] / h
    f_x = DistanceFromTarget(target, angles)
    angles[i] += SamplingDistance
    f_x_plius_d = DistanceFromTarget(target, angles)

    gradient = (f_x_plius_d - f_x) / SamplingDistance

    angles[i] = angles

    return gradient

def InverseKinematics(target, angles):
    global LR
    global DistanceThresh
    if (DistanceFromTarget(target, angles)<DistanceThresh):
        return 0
    for i in range(len(Joints), 0, -1):
        gradient = PartialGradient(target, angles,i )
        angles[i] =- LR * gradient
        if (DistanceFromTarget(target, angles)<DistanceThresh):
            return 0
        