import json
import requests
k = requests.get("https://frappe.io/api/method/frappe-library?page=2&title=and")
l = json.loads(k.text)
print(l)
with open("test.json","w") as sender:
    json.dump(l,sender,indent=4)