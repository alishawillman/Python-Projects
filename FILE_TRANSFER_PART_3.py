
from tkinter import *
import shutil
import time
import os
from tkinter import filedialog

root = Tk()
root.title('File Manager')
root.geometry("300x250")


def select_folder():
    filename = filedialog.askopenfilename(
        initialdir = "/", title = "Select a File",
        filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    print(filename)
    

def move_to():
    src = filedialog.askdirectory()
    dst = filedialog.askdirectory()

    SECONDS_IN_DAY = 24 * 60 * 60
    now = time.time()
    before = now - SECONDS_IN_DAY
    def last_mod_time(fname):
        return os.path.getmtime(fname)
    for fname in os.listdir(src):
        src_fname = os.path.join(src, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(dst, fname)
            shutil.move(src_fname, dst_fname)

def file_check():
    folderList = filedialog.askdirectory()
    sortlist = sorted(os.listdir(folderList))
    i=0
    print("Files in ", folderList, "folder are:")
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1
            

select_button = Button(root, text="Browse Files", command= select_folder)
select_button.pack(pady=20)

move_button = Button(root, text="Move To Folder", command= move_to)
move_button.pack(pady=22)

check_button = Button(root, text="File Check", command= file_check)
check_button.pack(pady=24)

root.mainloop()
