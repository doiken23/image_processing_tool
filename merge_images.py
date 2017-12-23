import numpy as np
import sys
import os
import time
from tqdm import tqdm

# get argument
def get_argument():
    args = sys.argv
    if len(args) != 4:
        print("arguments must be 2!!!\n"
             +"1: path of source image dir\n"
             +"2: path of source image dir\n"
             +"3: path of out dir\n")
        sys.exit()
    return args

# merge the images
def merge_img(img1, img2, out_path):
    out_array = np.concatenate((img1, img2), axis=0)
    np.save(out_path, out_array)

# do main implementation
if __name__ == '__main__':
    args = get_argument()
    source_dir1 = args[1]
    source_dir2 = args[2]
    out_dir = args[3]

    source_path_list1 = os.listdir(source_dir1)
    source_path_list1 = [os.path.join(source_dir1, image_path) for image_path in source_path_list1]
    source_path_list1.sort()
    source_path_list2 = os.listdir(source_dir2)
    source_path_list2 = [os.path.join(source_dir2, image_path) for image_path in source_path_list2]
    source_path_list2.sort()

    j = 0
    for i in tqdm(range(len(source_path_list1))):
        img1 = np.load(source_path_list1[i])
        img2 = np.load(source_path_list2[i])

        out_path = os.path.join(out_dir, source_path_list1[i].split('/')[-1].replace('RGBIR', 'RGBIRDSM'))
        merge_img(img1, img2, out_path)

        if j % 81 == 0:
            print('finish merging {} and {} into {}'.format(source_path_list1[i].split('/')[-1], source_path_list2[i].split('/')[-1], args[3].split('/')[-1]))

        j += 1
