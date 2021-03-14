import pickle
import time

def loaddict():
    try:
        with open("dictAcc.txt", "rb") as pkf:
            return pickle.load(pkf)
    except IOError:
        with open("dictAcc.txt", "w+") as pkf:
            pickle.dump(dict(), pkf)
            return dict()

def savedict(dictAcc):
    with open("dictAcc.txt", "wb") as pkf:
        pickle.dump(dictAcc, pkf)


def userPass():
    dictAcc = loaddict() #Load the dict
    checkAccount = raw_input("Do you have an account (Y or N)?")
    if (checkAccount == 'N' or checkAccount == 'n'):
        userName = raw_input("Please Set Your New Username: ")
        password = raw_input("Please Set Your New Password: ")
        if (userName in dictAcc):
            print("Username is taken")
            userPass()
        else:
            dictAcc[userName] = password
            print("Congratulations! You have succesfully created an account!")
            savedict(dictAcc) #Save the dict
            time.sleep(1.5)
            # dataInput() Code ends
    elif(checkAccount == 'Y' or checkAccount == 'y'):
        login()
    else:
        print("Invalid answer, try again")
        userPass()


def login():
    global userName
    global password
    global tries
    loginUserName = raw_input("Type in your Username: ")
    loginPass = raw_input("Type in your Password: ")
    dictAcc = loaddict() #Load the dict
    if (tries < 3):
        for key in dictAcc:
            if (loginUserName == key and loginPass == dictAcc[key]):
                print("You have successfully logged in!")
                # dataInput() Code ends
            else:
                print("Please try again")
                tries += 1
                login()
            if (tries >= 3):
                print("You have attempted to login too many times. Try again later.")
                time.sleep(3)
                tries=1 #To restart the tries counter
                login()

global tries
tries=1
userPass()