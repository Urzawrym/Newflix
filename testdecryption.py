from cryptography.fernet import Fernet, InvalidToken
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
decrypted = decrypted.decode("utf-8")

print(decrypted)
print(type(decrypted))
print(decrypted[0])

    #with open(output_file, 'wb') as f:
        #f.write(decrypted)  # Write the decrypted bytes to the output file

    # Note: You can delete input_file here if you want
#except InvalidToken as e:
    #print("Invalid Key - Unsuccessfully decrypted")