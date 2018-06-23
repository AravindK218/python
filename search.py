#!/usr/bin/python

obj1=open('data.txt','r')
for line in obj1:
    if "success" in line:
        print line
