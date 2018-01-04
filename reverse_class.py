import numpy as np
import sys
import os
import time
from PIL import Image
from tqdm import tqdm

# get argument
def get_argument():
    args = sys.argv
    if len(args) != 3:
        print("arguments must be 2!!!!\n"
              +"1: path of the image or directory.\n"
              +"2: path of the output directory.")
        sys.exit()
    return args

# change the image label
def reverse_label(arr):
    # getting the image array shape
    h, w = arr.shape[0], arr.shape[1]
    out_arr = np.zeros((h, w, 3))

    # reversing the labels
    out_arr[:, :, 0][np.where(arr==0)] = 255
    out_arr[:, :, 0][np.where(arr==4)] = 255
    out_arr[:, :, 0][np.where(arr==5)] = 255
    out_arr[:, :, 1][np.where(arr==0)] = 255
    out_arr[:, :, 1][np.where(arr==2)] = 255
    out_arr[:, :, 1][np.where(arr==3)] = 255
    out_arr[:, :, 1][np.where(arr==4)] = 255
    out_arr[:, :, 2][np.where(arr==0)] = 255
    out_arr[:, :, 2][np.where(arr==1)] = 255
    out_arr[:, :, 2][np.where(arr==2)] = 255

    return out_arr

# main program
def main():
    # get the arguments
    args = get_argument()
    images_path = os.path.abspath(args[1])
    output_dir = os.path.abspath(args[2])

    # get the image path list
    if os.path.isdir(images_path):
        image_path_list = os.listdir(images_path)
        image_path_list = [images_path+'/'+image_path for image_path in image_path_list if image_path[-3:] in ['tif', 'png', 'jpg']]
    else:
        image_path_list = [images_path]

    # implement the main program
    for image_path in tqdm(image_path_list):
        image = Image.open(image_path)
        array = np.array(image)

        out_array = reverse_label(array)
        out_path = output_dir + '/' + image_path.split('/')[-1][:-4] + '_labeled.png'
        Image.fromarray(out_array.astype(np.uint8)).save(out_path)

# implement the program
if __name__ == '__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("elapsed time:{0}".format(elapsed_time) + "[sec]")
