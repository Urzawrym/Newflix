import json
from cryptography.fernet import Fernet

users = [{"name": "Scott", "website": "stackabuse.com", "from": "Nebraska"}, {"name": "Larry", "website": "google.com", "from": "Michigan"}, {"name": "Tim", "website": "apple.com", "from": "Alabama"}]

#with open('exemple.json', 'w') as json_file:
    #json.dump(users, json_file)

#this generates a key and opens a file 'key.key' and writes the key there
key = Fernet.generate_key()
file = open('key.key','wb')
file.write(key)
file.close()

#this just opens your 'key.key' and assings the key stored there as 'key'
file = open('key.key','rb')
key = file.read()
file.close()

#this opens your json and reads its data into a new variable called 'data'
with open('exemple.json','rb') as f:
    data = f.read()

#this encrypts the data read from your json and stores it in 'encrypted'
fernet = Fernet(key)
encrypted=fernet.encrypt(data)

#this writes your new, encrypted data into a new JSON file
with open('exemple.json','wb') as f:
    f.write(encrypted)

decrypted = fernet.decrypt(encrypted)
print(decrypted)
print(type(decrypted))
print(decrypted.decode("utf-8"))
