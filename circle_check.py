import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

# Using circle equation, check the proximity for all of the points on the circle for a black value
# values obtained via centroid and radius
def circle_check(img,radius,centroid):
    test = np.array(img)
    cen_y,cen_x = centroid
    counter = 0
    for i in range(1, 361):
        x = (radius + 0.5) * math.cos(i)
        y = (radius + 0.5) * math.sin(i)
        x = int(cen_x + x)
        y = int(cen_y + y)
        for xx in range(-2,5):
            for yy in range(-2,3):
                if test[x+xx,y+yy] == 40:
                    counter = counter + 1
        if counter < 2:
            return False
        else:
            counter = 0
    return True

# draw a black circle around the centroid using circle equation
def circle_draw(img,radius,centroid):
    test = np.array(img)
    cen_y,cen_x = centroid
    counter = 0
    for i in range(1, 361):
        x = radius * math.cos(i)
        y = radius * math.sin(i)
        x = int(cen_x + x)
        y = int(cen_y + y)
        test[x,y] = 0
    return test
