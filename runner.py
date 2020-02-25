import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt
import closing, connected_label, threshold, circle_check


for x in range(1,16):
    #read in an image into memory
    img = cv.imread('Oring' + str(x) +'.jpg',0)
    before = time.time()
    tresh = threshold.get_threshold(img) - 60
    img = threshold.img_to_binary(img,tresh)
    img = closing.dialate(img)
    img = closing.erode(img)

    '''
    Image 13's interior holes can be filled by using closing multiple times
    however, this does not effect accuracy and harshly effects exectution time

    img = closing.dialate(img)
    img = closing.dialate(img)
    img = closing.dialate(img)
    img = closing.dialate(img)
    img = closing.dialate(img)
    img = closing.erode(img)
    img = closing.erode(img)
    img = closing.erode(img)
    img = closing.erode(img)
    img = closing.erode(img)
    '''

    img,centroid,radius = connected_label.connected_label(img)
    boolean = circle_check.circle_check(img,radius,centroid)
    after = time.time()
    img = circle_check.circle_draw(img,radius,centroid)
    exc_time = after - before

    # Put text on image for exectuion time
    text = 'exc = ' + str(exc_time)
    font = cv.FONT_HERSHEY_COMPLEX_SMALL
    org = (30, 210)
    fontScale = 0.5
    color = (0, 0, 0)
    thickness = 1
    img = cv.putText(img, text, org, font, fontScale,
                     color, thickness)

    if boolean == True:
        img = cv.putText(img, 'PASS', (15,20), cv.FONT_HERSHEY_SIMPLEX, fontScale,
                         color, thickness)
    else:
        img = cv.putText(img, 'FAIL', (15,20), cv.FONT_HERSHEY_SIMPLEX, fontScale,
                         color, thickness)
    #img = cv.circle(img,centroid,radius+1,color,thickness)
    cv.imshow('thresholded image 1',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
