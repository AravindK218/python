#!/usr/bin/python

data=raw_input("Enter something:")
print data[::-1]



sample=raw_input("Enter some data to test the palindrome:")
if sample == sample[::-1]:
    print "Entered data is Palindrome"
else:
    print "Entered data is String"
