
#importing packages
from tkinter import *
import shutil
import time
import os
from tkinter import filedialog

root = Tk()
root.title('File Manager')
root.geometry("600x200")

#tkinter widgets
def create_widgets():
    link_label = Label(root, text = "Select Files To Copy:")
    link_label.grid(row = 1, column = 0,
                    pady = 5, padx = 5)

    root.sourceText = Entry(root, width = 50,
                            textvariable = sourceLocation)
    root.sourceText.grid(row = 1, column = 1,
                         pady = 5, padx = 5,
                         columnspan = 2)

    source_browsebtn = Button(root,text = "Browse",
                              command = SourceBrowse, width = 15)
    source_browsebtn.grid(row = 1, column = 3,
                          pady = 5, padx = 5)

    destinationLabel = Label(root, text = "Select The Destination:")
    destinationLabel.grid(row = 2, column = 0,
                          pady = 5, padx = 5)
    root.destinationText = Entry(root, width = 50,
                                 textvariable = destinationLocation)
    root.destinationText.grid(row = 2, column = 1,
                              pady = 5, padx = 5,
                              columnspan = 2)
    dest_browsebtn = Button(root, text ="Browse",
                            command = DestinationBrowse, width = 15)
    dest_browsebtn.grid(row = 2, column = 3,
                        pady = 5, padx = 5)

    move_button = Button(root, text="Move Files", command= move_to, width = 15)
    move_button.grid(row = 3, column = 1,
                     pady = 5, padx = 5)

    check_button = Button(root, text="File Check", command= file_check, width = 15)
    check_button.grid(row = 3, column = 2,
                      pady = 5, padx = 5)
                             

def SourceBrowse():
    sourcedirectory = filedialog.askdirectory()
    root.sourceText.insert('1', sourcedirectory)

def DestinationBrowse():
    destinationdirectory = filedialog.askdirectory()
    root.destinationText.insert('1', destinationdirectory)
    

def move_to():
    source_location = sourceLocation.get()
    destination_location = destinationLocation.get()

    SECONDS_IN_DAY = 24 * 60 * 60
    now = time.time()
    before = now - SECONDS_IN_DAY
    def last_mod_time(fname):
        return os.path.getmtime(fname)
    for fname in os.listdir(sourceLocation.get()):
        src_fname = os.path.join(sourceLocation.get(), fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(destinationLocation.get(), fname)
            shutil.move(src_fname, dst_fname)

def file_check():
    filename = filedialog.askopenfilename(initialdir = "/", title = "File Check",
        filetypes = (("Text files","*.txt*"),("all files","*.*")))
    
sourceLocation= StringVar()
destinationLocation= StringVar()


create_widgets()
root.mainloop()
