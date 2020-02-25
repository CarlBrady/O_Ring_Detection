import cv2 as cv
import numpy as np

# compare each section of image to struct, if any of the image is the same then dialate whole section
def dialate(img):
    section = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0 ,0, 0]])

    struct = np.array([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])

    test = np.array(img)

    for i in range(2, img.shape[0] - 2):
        for j in range(2, img.shape[1] -2):
            countX = -1
            for z in range(i - 1,i + 2):
                countX = countX + 1
                countY = 0
                for y in range(j - 1,j + 2):
                    section[countX,countY] = img[z,y]
                    countY = countY + 1

            for z in range(-1,2):
                for y in range(-1,2):
                    if section[z,y] == struct [z,y]:
                       test[i,j] = 0
                       break;
                    else:
                       test[i,j] = img[i,j]


    return test

# compare each section of image to struct, if any of the image is the same then erode whole section
def erode(img):
    section = np.array([[0, 0, 0], [0, 0, 0],[0,0,0]])
    struct = np.array([[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]])
    test = np.array(img)
    for i in range(2, img.shape[0] - 2):
        for j in range(2, img.shape[1] -2):
            countX = -1
            for z in range(i - 1,i + 2):
                countX = countX + 1
                countY = 0
                for y in range(j - 1,j + 2):
                    section[countX,countY] = img[z,y]
                    countY = countY + 1
            if np.array_equal(section,struct) == True:
                test[i,j] = 0
            for z in range(-1,2):
                for y in range(-1,2):
                    if section[z,y] == 255:
                       test[i,j] = 255
                       break;
                    else:
                       test[i,j] = img[i,j]
    return test
