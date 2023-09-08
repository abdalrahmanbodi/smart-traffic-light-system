import os
import shutil

if __name__ == '__main__':
    file_image = 'C:\\Users\\abdal\\OneDrive\\Desktop\\image\\'
    file_lable = 'C:\\Users\\abdal\\OneDrive\\Desktop\\label\\'
    original_file_path ='C:\\Users\\abdal\\OneDrive\\Desktop\\fire-truck\\'
    
    for lable in os.listdir(original_file_path):
        if  lable[-4:] == ".jpg" :
            shutil.copy(original_file_path+lable,file_image+lable)
        else:
            shutil.copy(original_file_path+lable,file_lable+lable)
            
       

       