####################################################
##### This code is for making confusion matrix #####
##### the University of Tokyo Doi Kento        #####
####################################################

# import module
from PIL import Image
import numpy as np
import os
import glob
import sys
from sklearn.metrics import confusion_matrix

# get arguments
def get_arguments():
    args = sys.argv
    if len(args) != 5:
        print("Arguments should be 4!!!\n" +
              "1: inferenced image (directory) path\n" +
              "2: GT image (directory) path\n" +
              "3: out put directory\n" +
              "4: class number")
        sys.exit()
    return args

# make confusion matrix array
def make_confusion_matrix(GT_array, inferenced_array):
    reshape_num = inferenced_array.shape[0] * inferenced_array.shape[1]
    inferenced_array = np.reshape(inferenced_array, reshape_num)
    GT_array = np.reshape(GT_array, reshape_num)
    conf_array = confusion_matrix(GT_array, inferenced_array)
    return conf_array


def main():
    # get the arguments
    args = get_arguments()
    image_path = args[1]
    GT_path = args[2]
    out_dir = args[3]
    class_num = int(args[4])

    # make image path list
    if os.path.isdir(image_path):
        image_path_list = glob.glob(image_path + '/*')
        GT_path_list    = glob.glob(GT_path + '/*')
        image_path_list = [image_path for image_path in image_path_list if 'png' in image_path]
        GT_path_list = [GT_path for GT_path in GT_path_list if 'png' in GT_path]
    else:
        image_path_list = [image_path]
        GT_path_list    = [GT_path]
    image_path_list.sort()
    GT_path_list.sort()
    if len(image_path_list) != len(GT_path_list):
        print("image number is different!!!")
        sys.exit()

    # make one line array
    for i in range(len(image_path_list)):
        inferenced_array = np.array(Image.open(image_path_list[i]))
        GT_array         = np.array(Image.open(GT_path_list[i]))
        reshape_num = int(inferenced_array.shape[0] * inferenced_array.shape[1])
        inferenced_array = np.reshape(inferenced_array, reshape_num)
        GT_array = np.reshape(GT_array, reshape_num)
        if i == 0:
            pred = inferenced_array
            true = GT_array
        else:
            pred = np.concatenate((pred, inferenced_array), axis=0)
            true = np.concatenate((true, GT_array), axis=0)

    # make confusion matrix
    conf_mat = confusion_matrix(true, pred, labels=range(class_num))
    print(conf_mat)
    np.savetxt(os.path.join(out_dir, 'confusion_matrix.csv'), conf_mat, delimiter=',')

#-----------------------------
if __name__ == '__main__':
    main()



