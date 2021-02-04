import json
list2={'4':5,'6':7,'1':3,'2':5}
a=list(list2)
a.sort()
dic={}
for i in a:
    dic[i]=list2[i]
dic=json.dumps(dic,indent=4)
print(dic)