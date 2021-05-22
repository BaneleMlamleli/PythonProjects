import sys

smsBalance = 30
airtime = 100.00

def welcomeMenu():
    print("=====================\n"
    +"Welcome to ADF-Connect\n=====================\n"
    +"Press 1 : Data bundles\n"
    +"Press 2 : Check balance\n"
    +"Press 3 : Please call me\n"
    +"Press 4 : Exit\n"
    +"Please enter  a valid option: ")
    option = sys.stdin.readline()
    option = int(option)
    return option

def buyingBungles():
    global airtime
    print("=====================\n"
    +"  Buying Bundles\n"
    +"=====================\n"
    +"Press 1 : R2 for 10 mb\n"
    +"Press 2 : R4 for 20 mb\n"
    +"Press 3 : R6 for 30 mb\n"
    +"Press 4 : R8 for 50 mb\n"
    +"Press 5 : To go back to main menu\n"
    +"Please enter  a valid option: ")
    bundles = sys.stdin.readline()
    bundles = int(bundles)

    while bundles < 1 or bundles > 5:
        print("Error! please choose between 1 and 5: ")
        bundles = sys.stdin.readline()
        bundles = int(bundles)

    while bundles != 5:
        if bundles == 1:
            bundles = 1
            if airtime >= bundles:
                airtime = airtime - 2
                print("10 MB loaded")
            else:
                print("You have insufficient funds please load airtime")
        elif bundles == 2:
            bundles = 2
            if airtime >= bundles:
                airtime = airtime - 4
                print("20 MB loaded")
            else:
                print("You have insufficient funds please load airtime")
        elif bundles == 3:
            bundles = 3
            if airtime >= bundles:
                airtime = airtime - 6
                print("30 MB loaded")
            else:
                print("You have insufficient funds please load airtime")
        elif bundles == 4:
            bundles == 4
            if airtime >= bundles:
                airtime = airtime - 8
                print("50 MB loaded")
            else:
                print("You have insufficient funds please load airtime")

print(buyingBungles())