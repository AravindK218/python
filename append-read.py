#!/usr/bin/python env

data=raw_input("Please enter your data")
file= open("task.txt","a")
file.writelines(data)
file.close()

file2=open("task.txt","r")
for line in file2:
    print line
