# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”] 
import json
list1=["neelam","programer","2400"]
list2=["komal","tranier","2000"]
list3=["anuradha","HR","4000"]
list4=["abhisekh","manger","63000"]
data=dict(zip(list1,list2))
data1=dict(zip(list3,list4))
data=json.dumps(data,indent=4)
data1=json.dumps(data1,indent=4)
# data3=dict(zip(list3))
print(data)
print(data1)

