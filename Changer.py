import os

rootdir = 'C:/Users/Pieter/Documents/testmap/'
for dir in os.listdir(rootdir):
    fulldir = rootdir+dir
    for subdir in os.listdir(fulldir):
        new_name_split = subdir.split(None, 1)
        new_name = new_name_split.pop()
        os.rename(os.path.join(fulldir, subdir),
                  os.path.join(fulldir, new_name))
