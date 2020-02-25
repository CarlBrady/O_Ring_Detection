import cv2 as cv
import numpy as np
# function traverses image, if index item is black, the item is labelled and added to the queue. Each items direct neighbour is
# checked and if it is found to be black, it is labelled and added to the queue.
# function returns labelled image, centroid and radius
def connected_label(img):
    cur_lab = 40
    test = np.array(img)
    queue = []
    mean_x, mean_y, max_x, max_y, counter = 0,0,0,0,0
    min_x, min_y = 200,200
    centroid = (0,0)

    # checking all pixels in the image except border of two.
    for i in range(2, img.shape[0] - 2):
        for j in range(2, img.shape[1] -2):
            # if pixel is equal to the cur_lab value it is added to the queue
            if test[i,j] == 0:
                test[i,j] = cur_lab
                queue += [(i,j)]
            elif test[i,j] == cur_lab:
                cur_lab = 255
            # while the queue is full, check the neighbours of each item in the queue
            while queue != []:
                x,y = queue[0]
                #obtaining max and min x/y values
                if x > max_x and cur_lab == 40:
                    max_x = x
                elif x < min_x and cur_lab == 40:
                    min_x = x
                if y > max_y and cur_lab == 40:
                    max_y = y
                elif y < min_y and cur_lab == 40:
                    min_y = y
                mean_x += x
                mean_y += y
                counter += 1

                #if the neighbours of the queue item are black, label them and add the index to queue
                if test[x-1,y] == 0:
                    test[x-1,y] = cur_lab
                    mean_x += x-1
                    mean_y += y
                    counter += 1
                    queue += [(x-1,y)]
                if test[x+1,y] == 0:
                    test[x+1,y] = cur_lab
                    mean_x += x+1
                    mean_y += y
                    counter += 1
                    queue += [(x+1,y)]
                if test[x,y-1] == 0:
                    test[x,y-1] = cur_lab
                    mean_x += x
                    mean_y += y-1
                    counter += 1
                    queue += [(x,y-1)]
                if test[x,y+1] == 0:
                    test[x,y+1] = cur_lab
                    mean_x += x
                    mean_y += y+1
                    counter += 1
                    queue += [(x,y+1)]
                queue.pop(0)

    # radius obtained below by getting an average radius
    # from the max and min x/y compared to the mean x/y

    mean_x = mean_x/counter
    mean_y = mean_y/counter
    centroid = (int(mean_y),int(mean_x))
    radius_top = max_y - mean_y
    radius_bottom = mean_y - min_y
    radius_left = mean_x - min_x
    radius_right = max_x - mean_x
    radius = (radius_top + radius_bottom + radius_left + radius_right) /4


    return (test,centroid,int(radius))
