"""database={'name': '1234', 'name2': '5678', 'name3': '9012'}

def log():
    name = input('Enter username: ')
    ask = input('Enter pin: ')
    if name in database:
        if ask == database[name]: # changed this to an 'equals' rather than 'in'
            print ('Welcome', name)
        else:
            print ('Pin wrong!')
    else:
        print ('Username does not exist.')

log()"""


import json

filename = "users.json"
with open(filename, "r+", encoding='utf8') as file:
    '''opens json file and separates it by line by storing each line into an 
    array'''
    lines = file.readlines()

login_info = {}
'''array that will store usernames and passwords for each user(each line in 
the file is a user)'''



for line in lines:
    '''simply prints each element of the lines array displaying the 
    information of each user'''
    info = json.loads(line)
    print("USER: " + str(info))
    print("username: " + info["username"])
    print("password: " + info["password"] + "\n")
    login_info[info["username"]] = info["password"]
    '''creates a new pair of username and password for each user(each line is 
    a user)'''
    print(login_info)


print(lines)
print(login_info)

'''prompts user for their username and password'''
prompt_username = input("Please enter username: ")
prompt_password = input("Please input password: ")
login(prompt_username, prompt_password)

def login(username, password):
    '''if username exists and the inputed strings match one of the key-value
    pairs, login is successful returns (Username Correct, Password Correct)'''

    if username in login_info:
        if password == login_info[username]:
            print("LOGIN SUCCESSFUL")
            return (True, True)
        else:
            print("Sorry, password does not exist.")
            return (True, False)
    else:
        print("Sorry this username does not exist.")
        return (False, False)

login(prompt_username, prompt_password)