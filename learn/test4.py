import os
import shutil


a = r'D:\qq'
if os.path.exists(a):
    shutil.rmtree(a)
else:
    pass