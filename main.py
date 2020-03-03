import cv2 as cv
import numpy as np
import time
import matplotlib.pyplot as plt
import closing, connected_label, threshold, circle_check

for x in range(14,15):
    #read in an image into memory
    img = cv.imread('images/Oring' + str(x) +'.jpg',0)
    copy = cv.imread('images/Oring' + str(x) +'.jpg',0)


    before = time.time()
    tresh = threshold.get_threshold(img) - 60
    img = threshold.img_to_binary(img,tresh)
    img = closing.dialate(img)
    img = closing.erode(img)
    img,centroid,radius = connected_label.connected_label(img)
    boolean = circle_check.circle_check(img,radius,centroid)
    after = time.time()


    # Put text on image for exectuion time
    exc_time = after - before
    text = 'exc = ' + str(exc_time)
    font = cv.FONT_HERSHEY_COMPLEX_SMALL
    org = (30, 210)
    fontScale = 0.5
    color = (0, 0, 0)
    thickness = 1
    copy = circle_check.circle_draw(copy,radius,centroid)
    copy = cv.putText(copy, text, org, font, fontScale, color, thickness)
    if boolean == True:
        copy = cv.putText(copy, 'PASS', (15,20), cv.FONT_HERSHEY_SIMPLEX, fontScale, color, thickness)
    else:
        copy = cv.putText(copy, 'FAIL', (15,20), cv.FONT_HERSHEY_SIMPLEX, fontScale, color, thickness)
    #img = cv.circle(img,centroid,radius+1,color,thickness)
    #cv.imshow('Binary Image',img)

    cv.imshow('Image',copy)
    cv.waitKey(0)
    cv.destroyAllWindows()

    '''
    Image 13's interior holes can be filled by using closing multiple times
    however, this does not effect accuracy and harshly effects exectution time
    example =
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
