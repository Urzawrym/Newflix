from cryptography.fernet import Fernet
import json


message = "my deep dark secret".encode()  # .encode() is used to turn the string to bytes

file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

f = Fernet(key)
encrypted = f.encrypt(message)
decrypted = f.decrypt(encrypted)
decrypted = decrypted.decode()
print(decrypted)

try:
    with open("clients.json", "r") as f:
        dictclient = json.load(f)
except Exception:
    pass

