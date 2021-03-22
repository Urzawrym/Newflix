import json
import logintest

with open("users.json") as f:
    data = json.load(f)


new_dict = {"name": "name1",
             "Country": "Country2",
             "Gender": "Gender3"}


data["person"].append(new_dict)

with open("users.json", "w") as f:
    json.dump(data, f, indent=2)