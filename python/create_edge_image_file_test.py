import cv2
import numpy as np
import scipy.io as sio
img = cv2.imread('test_data/edge_map1.png')
assert img.shape == (256, 256, 3)
r = cv.resize(img[:,:,1], (320, 180))
r = np.expand_dims(r, axis=0)
r = np.expand_dims(r, axis=0)#(1, 1, 180, 320)
camera = np.zeros((1,9), dtype=int)
data_dict = dict()
data_dict['pivot_images'] = r
data_dict['positive_images'] =r # not actually used. Finn, in this case they seem to be the same image as pivot_images, which is just an edge image (I teted this by looking at three random images from the file train_10k)
data_dict['cameras'] = camera
sio.savemat('test_data/edge_image_file_test.mat',data_dict)