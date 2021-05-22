import os
import sys

upperCase = 'ABCDEFG'
lowerCase = 'abcdefg'

for letters in range(len(upperCase)):
    print(upperCase[letters]+str(letters))

'''
num = 100.00

#Method to test the use of a global variable
def firstFunc():
    global num
    opt = 'y'
    while opt != 'n':
        val = int(input('Enter a value: '))
        if val >= num:
            num - val
            print(val, ' >= ', num)
        else:
            num - val
            print(val, ' > ', num)
        print(num)
        opt = input('Again? y/n: ')

#Method to read, write and append a text file
def textFile():
    f = open('TextFile.txt', 'w')
    f.write("This a test of the text file I created to test the read, write and append modes")
    open('TextFile.txt').readlines()

textFile()
print(os.path.abspath(os.getcwd()))'''