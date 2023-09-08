import os
import shutil

if __name__ == '__main__':
    file_lable = 'C:\\Users\\abdal\\OneDrive\\Desktop\\Ambulance\\'
    save_path =  'C:\\Users\\abdal\\OneDrive\\Desktop\\x\\'
    

for lable in os.listdir(file_lable):
     if  lable[-4:]==".jpg" :
        shutil.copy(file_lable+lable,save_path+lable)
     if lable[-4:] ==".txt":
        new_file = open(save_path + lable, "a")
        f = open(file_lable + lable, "r")
        for x in f:
            list = x.split(' ')
            if list[0] == '4': 
                list[0] ="1"
                line=list[0]+" "+list[1]+" "+list[2]+" "+list[3]+" "+list[4]
                new_file.write(line)
            # elif list[0] == '1': 
            #     list[0] ="1"
            #     line=list[0]+" "+list[1]+" "+list[2]+" "+list[3]+" "+list[4]
            #     new_file.write(line)
            # elif list[0] == '2': 
            #     list[0] ="0"
            #     line=list[0]+" "+list[1]+" "+list[2]+" "+list[3]+" "+list[4]
            #     new_file.write(line)
            # elif list[0] == '3': 
            #     list[0] ="3"
            #     line=list[0]+" "+list[1]+" "+list[2]+" "+list[3]+" "+list[4]
            #     new_file.write(line)

            # else:
            #         list[0] ="1"
            #         line=list[0]+" "+list[1]+" "+list[2]+" "+list[3]+" "+list[4]
            #         new_file.write(line)
                        
        new_file.close()
        

