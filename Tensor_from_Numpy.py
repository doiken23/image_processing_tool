########################################
###### This script is made by Doi Kento.
###### University of Tokyo
########################################

# import torch module
import torch
import torch.utils.data as data_utils
from torch.autograd import Variable

# import python module
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import argparse

def get_argument():
    parser = argparse.ArgumentParser(description='Pytorch numpy-dataloader converter')
    parser.add_argument('image_dir_path', type=str, help='PATH of image directory.')
    parser.add_argument('out_dir_path', type=str, help='PATH of output directory.')
    parser.add_argument('out_name', type=str, help='output tensor name.')
    return parser.parse_args()

def main():
    # get the argument
    args = get_argument()

    # Loading the dataset
    print("Loading the numpy...")
    image_path_list = os.listdir(args.image_dir_path)
    image_path_list = [os.path.join(args.image_dir_path, image_path) for image_path in image_path_list]

    # get the image property
    image_shape = np.load(image_path_list[0]).shape
    image_height = image_shape[0]
    image_width = image_shape[1]
    band_number = image_shape[2]

    # convert the image_np to torch tensor
    ## prepare the empty tensor
    image_tensor = torch.zeros(len(image_path_list), image_height, image_width, band_number)

    ## convert numpy to tensor and put in big tensor
    print("Converting the numpy to the Tensor...")
    for i, npy in enumerate(image_path_list):
        data = np.load(npy)
        image_tensor[i,:,:,:] = torch.from_numpy(data)

    # confirm the tensor shape
    print(image_tensor.shape)

    # save the tensor
    out_name = args.out_name + '.tensor'
    torch.save(image_tensor, args.out_dir_path + '/' + out_name)

if __name__ == '__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print('elapsed_time:{0}'.format(elapsed_time) + "[sec]")
