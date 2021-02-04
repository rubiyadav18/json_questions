import json
# a Python object (dict):
python_obj = {
  "name": "rubi yadav",
  "class":"BA",
  "age": 17 
}
# convert into JSON:
data = json.dumps(python_obj,indent=4)
print(type(python_obj))

# result is a JSON string:
print(data)

