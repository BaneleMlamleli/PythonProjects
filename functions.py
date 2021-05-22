# -*- coding: cp1252 -*-
import math
import time
import sys
# -*- coding: cp1252 -*-
def testIfStatement(x, y):
    # Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y
    if x > y:
        return 1
    elif x == y:
            return 0
    elif x < y:
            return -1
            
    
def factorial(n):
    if n == 0:
        return 1
    else:
        recursion = factorial(n-1)
        result = n * recursion
        return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def whileCondition():
    n = raw_input("Enter looping value: ")
    int(n)
    while n > 0:
        print n
        n = n-1
        int(n)
    print 'Blastoff!'

def lenFunction():
    name = 'shaun'
    print len(name)
    print name[len(name)-1]

def backwardWord(word):
    wordLen = len(word)
    print word
    while wordLen != 0:
        print word[wordLen-1],
        wordLen -= 1

def testForLoop():
    for x in range(4,10,-2):
        print x

def sliceVariable():
    name = 'test_slices'
    xtr = name[0:4]
    print xtr
    print xtr[:2]
    print name[0:4] #slice all characters between 0 and 4
    print name[:4]  #slice all characters from start to the 4th
    print name[0:]  #slice all characters from 0 to the end
    print name[:]   #take everything

def readFile():
    fin = open('words.txt')
    for i in fin:
        word = i.strip()
        print word

'''Write a program that reads words.txt 
and prints only the words with more than
20 characters (not counting whitespace)'''
def readAndPrintWords():
    readFile = open('words.txt')
    for i in readFile:
        word = i.strip()
        if len(word) > 5:
            print word
        else:
            pass
    #print 'There are no words that are more than 20 characters int this file'

'''
Exercise 9.2.
1. Write a function called has_no_e that returns True if
   the given word doesn’t have the letter “e” in it.
2. Modify your program from the previous section to print
   only the words that have no “e” and compute the percentage
   of the words in the list have no “e.”
'''
def has_no_e():
    #word = raw_input("Enter a word: ")
    #print 'e' in word

    readFile = open('words.txt')
    per = 0.0
    wordsInc = 0
    wordCount = 0

    for word in readFile:
        found = word.find('e')
        if found != -1:
            wordsInc += 1
        else:
            wordCount +=1
            strWord = word.strip()
            print strWord
    per = (wordsInc/(wordsInc+wordCount))*100.0
    print str(per) + "%"

def findFunction():
    name = 'Banele'
    letterToFind = raw_input('Enter letter to find: ')
    print name.find(letterToFind,0,len(name))

#Test lists
def testLists():
    ages = [26, 34, 21]
    names = ['Banele', 'Hendrick', 'Shaun']
    mixList = []
    print ages*2    #repeating list
    print '============='
    mixList = ages[0:len(ages)]+names[0:len(ages)]  #slicing and concatenating lists
    mixList.append('one')   #add an element at the end of a list
    print mixList
    print '============='
    names.extend(ages)    #extend a list (can only extent using another list)
    print names
    print '============='
    names.sort()
    print names
    print '============='
    print names.pop(2)  # removes the element in the specified index
    print '============='
    del names[2]
    print names
    print '============='
    #traversing through a list
    for x in mixList:
        print x
        
'''Exercise 10.6. Write a function called is_sorted that takes a list as a
parameter and returns True if the list is sorted in ascending order and
False otherwise. You can assume (as a precondition) that the elements of
the list can be compared with the relational operators <, >, etc. 
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a'])
should return False.'''
def is_sorted():
    t = []
    inc = 3
    while inc != 0:
        value = raw_input("Enter value: ")
        t.append(value)
        inc -= 1
    t.sort()
    print t
    if t:
        print True
    else:
        print False

'''Exercise 10.10. Write a function that reads the file words.txt and builds
a list with one element per word. Write two versions of this function, one
using the append method and the other using the idiom t = t + [x]. Which one
takes longer to run? Why?'''
def addElementsToList():
    import time
    read = open("words.txt")
    for z in read:
        print z
