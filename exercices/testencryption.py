"""from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"Hello")
print(token)

print(f.decrypt(token))"""

import base64


print (base64.b64encode(b"Hello"))

#print (base64.b64decode(b"Hello"))




