import os
import shutil

if __name__ == '__main__':
    file_image = 'C:\\Users\\abdal\\OneDrive\\Desktop\\v\\train\\images\\'
    file_lable = 'C:\\Users\\abdal\\OneDrive\\Desktop\\v\\train\\labels\\'
    save_path =  'C:\\Users\\abdal\\OneDrive\\Desktop\\valid\\'
    classes_id = ['0','2','4','5','7']
    nw_path=''

for lable in os.listdir(file_lable):
    new_file = open(save_path + lable, "a")
    f = open(file_lable + lable, "r")
    for x in f:
        list = x.split(' ')
        for i in classes_id:
            if list[0] == i:
                new_file.write(x)
    new_file.close()
    if os.stat(save_path + lable).st_size == 0:
        os.remove(save_path+lable)
    else:
        nw_path=lable
    
    for image in os.listdir(file_image):
        if  nw_path[:-4] ==  image[:-4] :
            shutil.copy(file_image+image,save_path+image)
            nw_path=''