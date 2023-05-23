import os
import shutil
from_dir="C:/Users/Admin/Desktop/Bhakti Coding"
to_dir="C:/Users/Admin/Desktop/Document_Files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for i in list_of_files:
    root,ext=os.path.splitext(i)