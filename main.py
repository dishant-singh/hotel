from datetime import date
from datetime import time
import random
import pickle
import csv

def writestaff():
    """ Add a staff to the database """

    f = open("staffdetails.csv", "w")
    writer = csv.writer(f)
    writer.writerow(['Code', 'Name', 'Department', 'position', 'Gender'])
    rec = []
    ans = 'y'

    while ans == 'y':
        code = int(input('Enter the code:'))
        name = input('Enter the employee name:')
        dep = input('Enter the department:')
        pos = input('Enter the position:')
        g = input('Enter the gender:')
        lst = [code, name, dep, pos, g]
        rec.append(lst)
        print("##DATA SAVED##")
        ans = input("do you want to enter more record?(y/n):")

        if ans == 'n':
            print("thanks for chosing this ")

    writer.writerows(rec)
    f.close()

def readstaff():
    """ Read staff data from the database """

    with open("staffdetails.csv") as a:
        myreader = csv.reader(a, delimiter=",")
        print("%10s" % "CODE", "%10s" % "NAME", "%15s" % "DEPATMENT", "%10s" % "POSITION", "%10s" % "GENDER")
        print("="*84)
        for row in myreader:
            print("%10s" % row[0], "%15s" % row[1], "%15s" % row[2], "%20s" % row[3], "%10s" % row[4])

def checkout():
    f = open("customer.dat", "+ab")
    dt = date.today()
    print("=>CHECK OUT DATE->", dt)
    p = input("do you want to add more records - (y/n)==>")

    while p=="y"and"Y":
        f = open("customer.dat", "+ab")
        dt = date.today()
        print("=>CHECK OUT DATE->", dt)
        p = input("do you want to add more records - (y/n)==>")

    while p=="n"and"N":
        break

    print("*THANK YOU FOR COMMING PLEASE VISIT AGAIN*")
    f.close()

def check():
    f=open("check.dat","ab")
    print("\n\n""=>1(FOOD SERVICES)->")
    print("=>2.(ROOM SERVICES)->")
    ch=int(input("Enter the choice::"))

    if ch==1:
        print("\n""\t\t\t\t\t\t\t\t\t<---------------::HOTEL SERVICES::-------------->")
        print("\n""\t\t\t\t\t\t\t\t\t<---------------::FOOD SERVICES::-------------->")
        print("=>1.BREAKFAST")
        print("=>2.LUNCH")
        print("=>3.DINNER")
        F=int(input("ENTER THE CHOICE"))

        if F==1:
            fq=int(input("-->ENTER QUANTITY OF BREAKFAST(rs.40)=>"))
            fb=40*fq
            print("-->YOUE BILL OF FOOD IS=>",fb)

        elif F==2:
            fq=int(input("-->ENTER QUANTITY OF LUNCH(rs.100)=>"))
            fb=100*fq
            print("-->YOUE BILL OF FOOD IS=>", fb)

        elif F==3:
            fq = int(input("-->ENTER QUANTITY OF DINNER(rs.150)=>"))
            fb = 150*fq
            print("-->YOUE BILL OF FOOD IS=>", fb)

        else:
            print("::please select valid option::")

    elif ch==2:
        print("\n""\t\t\t\t\t\t\t\t\t<---------------::ROOM SERVICES::-------------->")
        print("=>1.AC")
        print("=>2.NON-AC")
        rc=int(input("=>ENTER THE CHOICE=>"))

        if rc==1:
            print("=>1.SINGLE BED")
            print("=>2.DOUBLE BED")
            sc=int(input("=>ENTER THE CHOICE=>"))

            if sc==1:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t*DONE*")
                sn=random.randint(0,100)
                print("-->ROOM TYPE==>", "\n->AC\n->SINGLE BED")
                print("=>YOUR ROOM NO. IS==>", sn)
                rb=1000
                print("\nYOUR BILL IS::",rb)

            elif sc==2:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t*DONE*")
                sn = random.randint(0, 100)
                print("-->ROOM TYPE==>", "\n->AC\n->DOUBLE BED")
                print("=>YOUR ROOM NO. IS==>",sn)
                rb =2000
                print("\nYOUR BILL IS::", rb)

        elif rc==2:
            print("=>1.SINGLE BED")
            print("=>1.DOUBLE BED")
            sc=int(input("=>ENTER THE CHOICE=>"))

            if sc==1:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t*DONE*")
                sn=random.randint(111,1000)
                print("-->ROOM TYPE==>", "\n->NON-AC\n->SINGLE BED")
                print("=>YOUR ROOM NO. IS==>", sn)
                rb=500
                print("\nYOUR BILL IS::",rb)

            elif sc==2:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t*DONE*")
                sn = random.randint(111,1000)
                print("-->ROOM TYPE==>", "\n->AC\n->DOUBLE BED")
                print("=>YOUR ROOM NO. IS==>",sn)
                rb =1500
                print("\nYOUR BILL IS::", rb)
    else:
        print("thank you")
    f.close()

def custumer():
    f = open("customer.dat", "wb")
    cn = (input("=>customer name->"))
    cids = random.randint(100000, 999999)
    print("=>customer id->", cids)
    cm = int(input("=>customer mobile no.->"))
    dt = date.today()
    print("=>check in date->", dt)
    d = {'customer name': cn, 'customer Id': cids, 'mobile no.': cm, 'date': dt}
    pickle.dump(d, f)
    p = input("do you want to add more records - (y/n)==>")

    while p == "y" and "Y":
        cn = (input("=>customer name->"))
        cids = random.randint(100000, 999999)
        print("=>customer id->", cids)
        cm = int(input("=>customer mobile no.->"))
        dt = date.today()
        print("=>check in date->", dt)
        p = input("do you want to add more records - (y/n)==>")
        d = {'customer name': cn, 'customer Id': cids, 'mobile no.': cm, 'date': dt}
        pickle.dump(d, f)

    while p == "n" and "N":
        break

    print("THANK YOU!")
    f.close()

def main():
    val = (input("TYPE y TO START; TYPE n TO EXIT: "))

    while(val!="n"):
        if (val=="y"):
            # Print MAIN MENU
            print(
                "\n""\t\t\t\t\t\t\t\t\t<---------------------------::WELCOME TO HOTEL PARADISE::------------------------->")
            print("\n""\t\t\t\t\t\t\t\t\t\t\t<---------------------------::MAIN MENU::------------------------->")
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t^_^(●'◡'●)^_^")
            print('\n'"=>1.Consumer Details-->")
            print("=>2.Staff    Details--> ")
            print("=>3.Exit-->")
            c = int(input("=>enter the choice::"))

            if c == 1:
                print("\n""\t\t\t\t\t\t\t\t\t\t\t\t\t<------------------::CONSUMER DETAILS::------------------>")
                print("\n""customer profile")
                print("=>1.check in")
                print("=>2.check out")
                print("=>3.search records")
                x = int(input("=>Enter the choice::"))

                if x == 1:
                    custumer()
                    check()
                elif x == 2:
                    checkout()
                elif x == 3:
                    print("work in proggress")
                else:
                    print("enter valid option")

            elif c == 2:
                print("2.staff details")
                print("records are")
                readstaff()

            elif c == 3:
                print("EXIT""\n""Thank You")

            else:
                print("=>please choose valid option-->")

        elif(val==0):
            break

        else:
            print("Incorrect value; please try agin.")

        val = (input("TYPE y TO START; TYPE n TO EXIT: "))

    print("Exiting..Thank you for using.")


if __name__ == "__main__":
    main()
