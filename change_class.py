import numpy as np
import sys
import os
import time
import cv2 
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
def change_label(arr):
    h, w, b = arr.shape
    out_arr = np.zeros((h, w, 1))
    out_arr += 0 * (np.all(arr == np.array([255,255,255]), axis=2))[:, :, np.newaxis]
    out_arr += 1 * (np.all(arr == np.array([0,0,255]), axis=2))[:, :, np.newaxis]
    out_arr += 2 * (np.all(arr == np.array([0,255,255]), axis=2))[:, :, np.newaxis]
    out_arr += 3 * (np.all(arr == np.array([0,255,0]), axis=2))[:, :, np.newaxis]
    out_arr += 4 * (np.all(arr == np.array([255,255,0]), axis=2))[:, :, np.newaxis]
    out_arr += 5 * (np.all(arr == np.array([255,0,0]), axis=2))[:, :, np.newaxis]

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
        image = cv2.imread(image_path)
        image = image[:,:,::-1]
        array = np.array(image)

        out_array = change_label(array)
        out_path = output_dir + '/' + image_path.split('/')[-1][:-4] + '_labeled.png'
        cv2.imwrite(out_path, out_array)

# implement the program
if __name__ == '__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("elapsed time:{0}".format(elapsed_time) + "[sec]")
