import os

rootdir = 'C:/Users/Pieter/Documents/testmap'

for subdir in os.walk(rootdir):
    print(rootdir.count())
    print(subdir)
