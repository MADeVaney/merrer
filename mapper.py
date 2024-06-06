#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

'''for line in sys.stdin: 
    line = line.strip() 
    words = line.split() 
    for word in words:
        print('%s\t%s' % (word, 1))'''

for line in sys.stdin:
    line = line.strip()
    word = ''
    for char in line:
        if char.isalpha():
            word += char
        elif word != '':
            print('%s\t%s' % (word, 1))
            word = ''
        