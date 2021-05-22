def addition(firstNumber, secNumber):
    sum = firstNumber+secNumber
    print (firstNumber +" + "+secNumber+" = "+sum)

def multiplication(firstNumber, secNumber):
    mult = firstNumber*secNumber
    print (firstNumber +" X "+secNumber+" = "+mult)

def subtraction(firstNumber, secNumber):
    sub = firstNumber-secNumber
    print (firstNumber +" - "+secNumber+" = "+sub)

def division(firstNumber, secNumber):
    if secNumber == 0:
        print "ERROR!! cannot divie be zero"
        while(secNumber == 0):
            secNumber = raw_input("Enter second number: ")
            secNumber = double(secNumber)
    else:
        div = firstNumber / secNumber
        print (firstNumber +" / "+secNumber+" = "+div)

print "\nCalculator program!!\n===================\n"
options = raw_input("A - Addition\nM - Multiplication\nS - Subtraction\nD - Division\nEnter option: ")
options = options.upper()

if(options == "A"):
    num = raw_input("First number: ")
    num = double(num)
    num1 = raw_input("Second number: ")
    num1 = double(num1)
    addition(num, num1)
elif options == "M":
    num = raw_input("First number: ")
    num = double(num)
    num1 = raw_input("Second number: ")
    num1 = double(num1)
    multiplication(num, num1)
elif options == "D":
    num = raw_input("First number: ")
    num = double(num)
    num1 = raw_input("Second number: ")
    num1 = double(num1)
    division(num, num1)
elif options == "S":
    num = raw_input("First number: ")
    num = double(num)
    num1 = raw_input("Second number: ")
    num1 = double(num1)
    multiplication(num, num1)
else:
    print "Error! select within the provided options"