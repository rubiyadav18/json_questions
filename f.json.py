import json
dict={
    "name":"govind",
    "age":"17",
    "from":"navgurukul",
    "class":"BA"
    }
file=open("f.json","w")
filedata=json.dumps(dict,indent=5)
file.write(filedata)
file.close()