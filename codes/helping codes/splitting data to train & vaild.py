import os
from random import choice
import shutil

#arrays to store file names
imgs =[]
txt =[]

#setup dir names
trainPath = 'C:\\Users\\abdal\\OneDrive\\Desktop\\train\\'
# valPath = 'C:\\Users\\abdal\\OneDrive\\Desktop\\final_data\\valid\\'
valPath = ''
original_path = 'C:\\Users\\abdal\\OneDrive\\Desktop\\final_data (train5)\\' #dir where images and annotations stored

#setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
train_ratio = 0.8
validation_ratio = 0.2


#total count of imgs
totalImgCount = len(os.listdir(original_path))/2

#sorting files to corresponding arrays
for (dirname, dirs, files) in os.walk(original_path):
    for filename in files:
        if filename.endswith('.txt'):
            txt.append(filename)
        else:
            imgs.append(filename)


#counting range for cycles
countForTrain = int(len(imgs)*train_ratio)
countForvalidation = int(len(imgs)*validation_ratio)

#cycle for train dir
for x in range(countForTrain):

    fileJpg = choice(imgs) # get name of random image from origin dir
    filetxt = fileJpg[:-4] +'.txt' # get name of corresponding annotation file

    #move both files into train dir
    shutil.move(os.path.join(original_path, fileJpg), os.path.join(trainPath, fileJpg))
    shutil.move(os.path.join(original_path, filetxt), os.path.join(trainPath, filetxt))

    #remove files from arrays
    imgs.remove(fileJpg)
    txt.remove(filetxt)

#rest of files will be validation files, so rename origin dir to val dir
os.rename(original_path, valPath)

