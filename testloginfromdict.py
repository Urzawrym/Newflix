myList = [{'foo':12,'bar':14},{'moo':52,'bar':641},{'doo':6,'tar':84}]

"""print(myList[0])
print(myList[0]['bar'])

print(myList[1])
print(myList[1]['moo'])

print(myList[2])
print(myList[2]['doo'])"""

login = 12
password = 641

if any(d["foo"] == login for d in myList) and any(d["bar"] == password for d in myList):
    print("yeah")



