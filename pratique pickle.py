# Save a dictionary into a pickle file.

import pickle
import base64

users = {"claude": "1234", "mathieu": "royer","meo":"8907"}



pickle.dump((base64.b64encode(users)), open("modifuser.p", "wb"))

"""def trylist():
    with open("modifuser.p", "rb") as modifile:
        return pickle.load(modifile)

listuser = trylist()
print(listuser)"""


"""data = base64.urlsafe_b64decode(request.form['pickled'])
    deserialized = pickle.loads(data)"""

