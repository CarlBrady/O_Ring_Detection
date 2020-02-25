import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# converts image to black or white depending on threshold value
def img_to_binary(img,thresh):
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if img[i,j] > thresh:
                img[i,j] = 255
            else:
                img[i,j] = 0
    return img

# get_threshold returns the most frequent value in image
def get_threshold(img):
    hist = np.zeros(256)
    most_freq = np.zeros(256)
    empty = np.zeros(256)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            hist[img[i,j]]+=1
            if hist[img[i,j]].all() > most_freq.all(): #
                x = img[i,j]#
    return x
