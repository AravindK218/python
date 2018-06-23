#!/usr/bin/python


file=open("data.txt","r")
for line in file:
    if 'success' in line:
        print line
    '''if 'failure' in line:
            print line'''
