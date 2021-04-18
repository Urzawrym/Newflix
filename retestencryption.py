from cryptography.fernet import Fernet, InvalidToken


file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()


input_file = 'test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the input file

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)  # Write the encrypted bytes to the output file

# Note: You can delete input_file here if you want