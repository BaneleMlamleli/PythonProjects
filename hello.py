import random
import os

#LIST
def listFunction():
    listName = list()
    emptyList = list()
    listName = ['Banele', 'Hendrick', 'Shaun', 'Mlamleli']
    listName.append('Sethu')
    nestedList = [1,2,3,['one', 'two', 'three'], True, False]
    nestedList[3][2] = ['four']
    nestedList[3:4] = [4]
    concatList = listName[0:3] + nestedList[0:3]
    zipList = zip(nestedList, concatList)
    emptyList.extend(concatList)
    print emptyList
    emptyList.sort()
    print emptyList
    del emptyList[:]
    print emptyList
    emptyList = list('BaneleMlamleli')
    print emptyList
    name = 'ba_ne_le'
    print name.split('_')
    ls = list(name.split('_'))
    print ls
    print listName
    print zipList
    print concatList
    print nestedList

#DICTIONARY
def dictionary():
    dictName = dict()
    dictName = {1:'one', 2:'two', 3:'three'}

#TUPLES
def tuples():
    tupleName = tuple()
    tupleName = (1, 'one', 2, 'two', 2.9, True, 2**3)
    print tupleName
    for index, element in enumerate(tupleName):
        print index, element

def evenNumber():
    for i in range(10):
        if (i % 2) == 0:
            print i

def randomNumbers():
    print random.randint(5,10)
    t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print random.choice(t)

def compTuples():
    print (1, 1) < (1, 2)

def files():
    openFile = open('words.txt', 'w')
    print openFile

def exception():
    try:
        num = int(input('Enter value: '))
    except (NameError), e:
        print('Error! ', e)
    else:
        print('Entered number ', int(num))

exception()