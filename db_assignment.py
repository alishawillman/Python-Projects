

import sqlite3

conn = sqlite3.connect('assignmentDB.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_files TEXT \
                )")
    conn.commit()

conn = sqlite3.connect('assignmentDB.db')

# Tuple of files
files_tuple = ('information.docx', 'Hello.txt', 'myImage.png',
               'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Loop through to find files that end with .txt
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileList (col_files) VALUES (?)", (x,))
            print(x)
conn.close()
