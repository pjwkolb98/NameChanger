import os

rootdir = 'C:/Users/Pieter/Documents/testmap/'

for dir in os.listdir(rootdir):
    print(dir)
    new_name_split = dir.split(None, 1)
    new_name = new_name_split.pop()
    print(new_name)
    os.rename(os.path.join(rootdir, dir),
              os.path.join(rootdir, new_name))
