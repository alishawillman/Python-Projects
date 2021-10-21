import webbrowser

#creates an html file
f = open("webpagegen.html", "w")
f.write("Stay tuned for our amazing summer sale!")
f.close()

url = 'webpagegen.html'
webbrowser.open(url, new=2) #open in a new tab

from tkinter import *

root = Tk()
root.title('Web Page Generator')
root.geometry("500x450")

def open_html():
    html_file = open("webpagegen.html", 'r')
    html = html_file.read()
    my_text.insert(END, html)
    html_file.close()

def update_html():
    html_file = open("webpagegen.html", 'w')
    html_file.write(my_text.get(1.0, END))

my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20) 

open_button = Button(root, text="Open HTML File", command = open_html)
open_button.pack(pady=20)

update_button = Button(root, text="Update File", command= update_html)
update_button.pack(pady=20)

root.mainloop()
