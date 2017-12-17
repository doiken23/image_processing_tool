#############################################
##### This is script for compute        #####
##### median frequency balancing weight #####
##### University of Tokyo Doi Kento     #####
#############################################

# import python liblary
import numpy as np
from PIL import Image
import os
import argparse
import time
from tqdm import tqdm

def get_argument():
    parser = argparse.ArgumentParser(description='Compute Weight')
    parser.add_argument('image_dir', type=str, help='path of label image directory')
    parser.add_argument('out_dir', type=str, help='path of output directory')
    parser.add_argument('class_num', type=int, help='class number')
    args = parser.parse_args()
    return args

def compute_weight(args):
    # this function read the images and compute the median frequency balancing
    
    # get the image path list
    image_path_list = os.listdir(args.image_dir)
    image_path_list = [image_path for image_path in image_path_list if image_path[-3:] == 'png']
    image_path_list = [os.path.join(args.image_dir, image_path) for image_path in image_path_list]

    # read the image and compute the weight
    pixel_num = np.zeros(args.class_num)
    for image_path in tqdm(image_path_list):
        # read the images
        image = Image.open(image_path)
        array = np.array(image)

        # compute the pixel number
        for i in np.arange(args.class_num):
            pixel_num[i] += (array == i).sum()

    # compute the median frequency weight
    weight = np.zeros(args.class_num)
    weight = np.median(pixel_num) / pixel_num
    
    np.save(os.path.join(args.out_dir, 'weght.npy'), weight)
    return weight

def main():
    args = get_argument()
    weight = compute_weight(args)
    print('medin frequency balancing is...')
    print(weight)

############################
# implement the main program
if __name__ == '__main__':
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print('elapsed time: {} [sec]'.format(elapsed_time))
