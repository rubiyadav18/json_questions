import json
dic={
    "emp1":{
        "name":"rubi",
        "age":23,
        "salary":23000,
    "emp2":{
        "name":"jyoti",
        "age":19,
        "salary":40000,
    "emp3":{
        "name":"pragati",
        "age":25,
        "salary":20000,
    "emp4":{
        "name":"mohini",
        "age":40,
        "salary":50000,
    }
    }
    }
    }
}
    
with open("myfile.json","w") as f:
    json.dump(dic,f,indent=4)
    print(dic)
    print(type(dic))
