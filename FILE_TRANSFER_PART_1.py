


#transfering files from one folder to another
import shutil
import os

#set where the source of the files are
source = '/Users/14065/Documents/Github/Python-Projects/Folder_A/'

#set the destination path to folderB
destination = '/Users/14065/Documents/Github/Python-Projects/Folder_B/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
