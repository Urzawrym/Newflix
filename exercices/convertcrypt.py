from cryptography.fernet import Fernet, InvalidToken
from ast import literal_eval

file = open('../key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

fernet = Fernet(key)

"""input_file = 'test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the input file

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)  # Write the encrypted bytes to the output file

# Note: You can delete input_file here if you want"""

with open("films.json", "rb") as file:
    data = file.read()



#with open("filmscrypt.json", "wb") as file:
    #usercrypt = fernet.encrypt(data)
    #file.write(usercrypt)



with open("../filmscrypt.json", "rb") as file:
    file_data = file.read()
    datacrypt = fernet.decrypt(file_data)
    dictdata = literal_eval(datacrypt.decode('utf8'))

print(dictdata)

print(type(dictdata))

"""newdict = {"nom": "Avatar", "duree": "02:15", "descriptionfilm": "Elle ava tord", "categories": [{"nom": "action", "description": "ca bouge"}, {"nom": "science-fiction", "description": "dans le futur"}], "acteurs": [{"nom": "Willis", "prenom": "Bruce", "sexe": "Masculin", "nompersonnage": "TiClin", "debutemploi": "12-05-2020", "finemploi": "12-07-2020", "cachet": "400000"}]}

dictdata.append(newdict)



datab = str(dictdata)

finaldata = datab.encode('utf8')

print(type(finaldata))

with open("filmscrypt.json", "wb") as file:
    usercrypt = fernet.encrypt(finaldata)
    file.write(usercrypt)

with open("filmscrypt.json", "rb") as file:
    file_data = file.read()
    datacrypt = fernet.decrypt(file_data)
    dictdata = literal_eval(datacrypt.decode('utf8'))

print(dictdata)"""