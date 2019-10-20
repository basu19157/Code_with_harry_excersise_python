# Health Management System
# 3 clients - basu, tushar and siraj

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
import datetime
def gettime():
    
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for kills and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("basu-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("basu-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for kills and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("tushar-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("tushar-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for kills and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("siraj-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("siraj-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(basu),2(tushar),3(siraj)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for kills and 2 for food"))
        if(c==1):
            with open("basu-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("basu-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for kills and 2 for food"))
        if (c == 1):
            with open("tushar-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("tushar-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for kills and 2 for food"))
        if (c == 1):
            with open("siraj-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("siraj-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (basu,tushar,siraj)")
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for basu 2 for tushar 3 for siraj "))
    take(b)
else:
    b = int(input("Press 1 for basu 2 for tushar 3 for siraj "))
    retrieve(b)
  
