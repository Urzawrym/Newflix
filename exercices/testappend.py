import json
import newflix

"""with open("users.json") as f:
    data = json.load(f)


new_dict = {"name": "name1",
             "Country": "Country2",
             "Gender": "Gender3"}


data["person"].append(new_dict)

with open("users.json", "w") as f:
    json.dump(data, f, indent=2)"""

with open("testuser.json", "r+") as f:
    dic = json.load(f)
    print(dic)