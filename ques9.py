import json 
data={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
	}
coustmer=input("which items do u want to buy")
coustmper1=int(input("enter how many items do u want buy"))
del data ["shopping_list"][coustmer]
print(data["shopping_list"])
coustmer2=input("enter a which oitms do u want add")
coustmer4=int(input("enter  a haw many itms do u add"))
data ["shopping_list"][coustmer2]=coustmer4
file=open("shopping_list.json","w")
filedata=json.dump(data,file,indent=4)
file.close()
f=json.dump(data,indent=4)
print(f)


































