import sys

NrTickets = 0  # Total amount of all the tickets
GrandTot = 0.0  # Total amount of all ticket sales
CustTot = 0.0  # Total cost for customer for all locations

print("")
print("************ CTownTours - your doorway to CapeTown **************")
print("")
print("New customer? (Y/N) >> ")
NewCust = sys.stdin.readline()
NewCust = NewCust[0].upper()
# this code will allow the user to re-enter either Y/N if they entered option incorrect
while (NewCust != 'N') & (NewCust != 'Y'):
    print("Invalid option, please enter Y or N >> ")
    NewCust = sys.stdin.readline()
    NewCust = NewCust[0].upper()

if NewCust == 'N':
    print("==========================================================================")
    print("*****NO TICKET SALES THE WHOLE DAY...*****")
elif NewCust == 'Y':
    while NewCust != 'N':
        # The below code is for checking if the option entered matches with that in the options
        print("Enter a location (A=Aquarium, B=caBlecar, C=Castle, K=Kirstenbosch, or X to stop) >> ")
        Location = sys.stdin.readline()
        Location = Location[0].upper()
        # this code will allow the user to re-enter either Y/N if they entered option incorrectly
        while (Location != 'A') & (Location != 'B') & (Location != 'C') & (Location != 'K') & (Location != 'X'):
            print("Invalid location, please re-enter (A, B, C, K or X to stop) >> ")
            Location = sys.stdin.readline()
            Location = str(Location[0].upper())

        if Location == 'X':
            print ("*****NO LOCATIONS FOR THIS CUSTOMER...*****")
        else:
            while Location != 'X':
                # Location is an Aquarium
                if Location == 'A':
                    print("How many adults? >> ")
                    QtyAdults = sys.stdin.readline()
                    QtyAdults = int(QtyAdults)
                    while QtyAdults < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyAdults = sys.stdin.readline()
                        QtyAdults = int(QtyAdults)

                    print("How many children? >> ")
                    QtyKids = sys.stdin.readline()
                    QtyKids = int(QtyKids)
                    while QtyKids < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyKids = sys.stdin.readline()
                        QtyKids - int(QtyKids)

                    # if amount of kids is more than that of adults
                    if QtyKids > QtyAdults:
                        kids = QtyKids - QtyAdults
                        TotPrice = (kids * 60.00) + (QtyAdults * 150.00)
                        NrTickets = NrTickets + (kids + QtyAdults)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Aquarium: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults == QtyKids:
                        TotPrice = QtyAdults * 150.00
                        NrTickets = NrTickets + (QtyAdults * 2)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Aquarium: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults > QtyKids:
                        TotPrice = QtyAdults * 150.00
                        NrTickets = NrTickets + QtyAdults
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the " + Location + ": R" + str(TotPrice) + "<<<<<")

                # Location is to the caBlecar
                elif Location == 'B':
                    print("How many adults? >> ")
                    QtyAdults = sys.stdin.readline()
                    QtyAdults = int(QtyAdults)
                    while QtyAdults < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyAdults = sys.stdin.readline()
                        QtyAdults = int(QtyAdults)

                    print("How many children? >> ")
                    QtyKids = sys.stdin.readline()
                    QtyKids = int(QtyKids)
                    while QtyKids < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyKids = sys.stdin.readline()
                        QtyKids = int(QtyKids)

                    # if amount of kids is more than that of adults
                    if QtyKids > QtyAdults:
                        kids = QtyKids - QtyAdults
                        TotPrice = (kids * 100.00) + (QtyAdults * 150.00)
                        NrTickets = NrTickets + (kids + QtyAdults)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Cablecar: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults == QtyKids:
                        TotPrice = QtyAdults * 150.00
                        NrTickets = NrTickets + (QtyAdults * 2)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Cablecar: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults > QtyKids:
                        TotPrice = QtyAdults * 150.00
                        NrTickets = NrTickets + QtyAdults
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Cablecar: R" + str(TotPrice) + "<<<<<")

                # Location is to Castle
                elif Location == 'C':
                    print("How many adults? >> ")
                    QtyAdults = sys.stdin.readline()
                    QtyAdults = int(QtyAdults)
                    while QtyAdults < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyAdults = sys.stdin.readline()
                        QtyAdults = int(QtyAdults)

                    print("How many children? >> ")
                    QtyKids = sys.stdin.readline()
                    QtyKids = int(QtyKids)
                    while QtyKids < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyKids = sys.stdin.readline()
                        QtyKids = int(QtyKids)

                    # if amount of kids is more than that of adults
                    if QtyKids > QtyAdults:
                        kids = QtyKids - QtyAdults
                        TotPrice = (kids * 25.00) + (QtyAdults * 75.00)
                        NrTickets = NrTickets + (kids + QtyAdults)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Castle: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults == QtyKids:
                        TotPrice = QtyAdults * 75.00
                        NrTickets = NrTickets + (QtyAdults * 2)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Castle: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults > QtyKids:
                        TotPrice = QtyAdults * 75.00
                        NrTickets = NrTickets + QtyAdults
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Castle: R" + str(TotPrice) + "<<<<<")

                # Location is Kirstenbosch
                elif Location == 'K':
                    print("How many adults? >> ")
                    QtyAdults = sys.stdin.readline()
                    QtyAdults = int(QtyAdults)
                    while QtyAdults < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyAdults = sys.stdin.readline()
                        QtyAdults = int(QtyAdults)

                    print("How many children? >> ")
                    QtyKids = sys.stdin.readline()
                    QtyKids = int(QtyKids)
                    while QtyKids < 0:
                        print("Invalid quantity, please re-enter a value of 0 or more >> ")
                        QtyKids = sys.stdin.readline()
                        QtyKids = int(QtyKids)

                    # if amount of kids is more than that of adults
                    if QtyKids > QtyAdults:
                        kids = QtyKids - QtyAdults
                        TotPrice = (kids * 15.00) + (QtyAdults * 50.00)
                        NrTickets = NrTickets + (kids + QtyAdults)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for Kirsternbosch: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults == QtyKids:
                        TotPrice = QtyAdults * 50.00
                        NrTickets = NrTickets + (QtyAdults * 2)
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Kirsternbosch: R" + str(TotPrice) + "<<<<<")
                    elif QtyAdults > QtyKids:
                        TotPrice = QtyAdults * 50.00
                        NrTickets = NrTickets + QtyAdults
                        CustTot = CustTot + TotPrice
                        GrandTot = GrandTot + TotPrice
                        print (">>>>>Total cost for " + str(QtyAdults) + " adults and " + str(
                            QtyKids) + " children for the Kirsternbosch: R" + str(TotPrice) + "<<<<<")

                # The below code is for checking if the option entered matches with that in the options
                print("Enter a location (A=Aquarium, B=caBlecar, C=Castle, K=Kirstenbosch, or X to stop) >> ")
                Location = sys.stdin.readline()
                Location = Location[0].upper()
                while (Location != 'A') & (Location != 'B') & (Location != 'C') & (Location != 'k') & (Location != 'X'):
                    print("Invalid location, please re-enter (A, B, C, K or X to stop) >> ")
                    Location = sys.stdin.readline()
                    Location = str(Location[0].upper())

            print (">>>>> Total Amount Due: R"+str(CustTot)+" <<<<<")

        #The below code is for checking if there is a new customer or not
        print("New customer? (Y/N) >> ")
        NewCust = sys.stdin.readline()
        NewCust = NewCust[0].upper()
        #This code will allow the user to re-enter either Y/N if the entered option is incorrect
        while (NewCust != 'N') & (NewCust != 'Y'):
            print("Invalid option, please enter Y or N >> ")
            NewCust = sys.stdin.readline()
            NewCust = NewCust[0].upper()

    print (">>>>> Total Sales for the day: R"+str(GrandTot)+" <<<<<>>>>> Total Number of Tickets sold: "+str(NrTickets)+" <<<<<")
