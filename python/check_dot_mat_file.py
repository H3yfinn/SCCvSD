import scipy.io as sio
import mat4py
data = sio.loadmat('deep/train_data_10k.mat')
new_dict = dict()
new_dict['pivot_images'] = data['pivot_images'][5000]
new_dict['positive_images'] = data['positive_images'][5000]
new_dict['cameras'] = data['cameras'][5000]
sio.savemat('single_entryfromtraindata_test.mat', new_dict)

#print(data.keys())