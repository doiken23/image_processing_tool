import numpy as np
import cv2
import os, sys, time

### get the argment
def get_argment():
    args = sys.argv
    if len(args) != 6:
        print("argments must be 4!!!!\n"
               + "1: path of image or directory.\n"
               + "2: path of the output directory.\n"
               + "3: cropping size.\n"
               + "4: stride.\n"
               + "5: flag.(if band is 1 band, flag should be 0. else 1"
                )
        sys.exit()
    return args

### crop the image and save as *.py
def crop_save_images(image_path, output_dir, crop_size, stride):
    # read the image
    if flag == 0:
        image_array = cv2.imread(image_path, flag)
    else:
        image_array = cv2.imread(image_path)
    (h, w, c) = image_array.shape

    # compute the window number
    X = (w - crop_size)//stride + 1
    Y = (h - crop_size)//stride + 1
    for j in range(Y):
        for i in range(X):
            y = j * stride
            x = i * stride
            patch_array = image_array[y: y + crop_size, x: x + crop_size, :]
            if flag == 0:
                path_array[:, :, np.newaxis]
            patch_array = np.transpose(patch_array, (2,0,1))
            output_image_name = image_path[:-4] + '_{}_{}'.format(str(j), str(i))
            output_path = os.path.join(output_dir, output_image_name.split('/')[-1])
            np.save(output_path, patch_array)

### main program
def main():
    # get the argments
    args = get_argment()
    images_path = os.path.abspath(args[1])
    output_dir = os.path.abspath(args[2])
    crop_size = int(args[3])
    stride = int(args[4])
    flag = int(args[5])

    # get the image path list
    if os.path.isdir(images_path):
        image_path_list = os.listdir(images_path)
        image_path_list = [images_path+'/'+image_path for image_path in image_path_list if image_path[-3:] in ['tif', 'jpg', 'png'] ]
    else:
        image_path_list = [images_path]

    # implement the main roop
    for image_path in image_path_list:
        crop_save_images(image_path, output_dir, crop_size, stride)
        print('Complete saving the {}......'.format(image_path.split('/')[-1]))


### implement the program
if __name__ == '__main__':
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("elapsed time:{0}".format(elapsed_time) + "[sec]")

