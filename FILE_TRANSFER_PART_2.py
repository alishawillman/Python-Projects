


import time
import os
import shutil

SECONDS_IN_DAY = 24 * 60 * 60

src = '/Users/14065/Documents/Github/Python-Projects/Created_Modified(24hrs)/'
dst = '/Users/14065/Documents/Github/Python-Projects/Created_Modified(copies)/'

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.move(src_fname, dst_fname)
