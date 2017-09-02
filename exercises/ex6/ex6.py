# -*- coding: utf-8 -*-
"""
Then create a script that merges the three text files into a new text file 
containing the text of all three files. 
The filename of the merged text file should contain the current timestamp down 
to the millisecond level. E.g. "2016-06-01-13-57-39-170965.txt".
"""

def getfiledata(filename):
    f = open(filename,'r')
    read_data=f.read()
    f.close
    return read_data

import datetime
destfile_name= datetime.datetime.now()
destfile_name=destfile_name.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"

flist=["file1.txt","file2.txt","file3.txt"] #list of the files to be open

#open file with "with" method so it closes automatically
with open(destfile_name,'a') as destfile:
    for file in flist: #iterate the file list to open each file
        destfile.write(getfiledata(file)+"\n")
        