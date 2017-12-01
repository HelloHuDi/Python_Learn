import json

numberList = list(x ** 2 for x in range(1, 200) if x % 2 == 0)

dumpfile_name = "testFile/dump.json"
with open(dumpfile_name, "w") as json_object:
    json.dump(numberList, json_object)
    print(len(numberList))

with open(dumpfile_name, "r") as json_object:
    numberListLoad = json.load(json_object)
    print(numberListLoad)
    print(len(numberListLoad))
    print(numberList == numberListLoad)
