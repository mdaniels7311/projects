import json
complexList = [
    [1,2,3,4,5,6,7,8,9],
    [10,21,30,40,50,69,70,80,90],
    [100,200,300,400,500,600,700,800,900]
    ]

with open("jsonFile.txt",mode="w", encoding="utf-8") as file:
    json.dump(complexList,file)

with open("jsonFile.txt",mode="r", encoding="utf-8") as file:
    newlist = json.load(file)

print(complexList)
print(newlist)
