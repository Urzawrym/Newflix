from cryptography.fernet import Fernet, InvalidToken
from ast import literal_eval

file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()
input_file = 'test.encrypted'
output_file = 'testfinal.txt'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the encrypted file

fernet = Fernet(key)
#try:
decrypted = fernet.decrypt(data)

data = literal_eval(decrypted.decode('utf8'))

print(decrypted)
print(type(decrypted))
print(data)
print(type(data))

for dict in data:
    print(dict["nom"])
    #with open(output_file, 'wb') as f:
        #f.write(decrypted)  # Write the decrypted bytes to the output file

    # Note: You can delete input_file here if you want
#except InvalidToken as e:
    #print("Invalid Key - Unsuccessfully decrypted")