import json 
   
# Data to be written 
dictionary ={ 
    "name" : "rubi yadav", 
    "rollno" : 40, 
    "cgpa" : 8.6, 
    "phonenumber" : "7408080615"
} 
   
with open("sample.json", "w") as outfile: 
    json.dump(dictionary, outfile) 