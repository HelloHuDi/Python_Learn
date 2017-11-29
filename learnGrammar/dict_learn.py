dict = {"hd": "12", "ds": "12w", "sd": "12we"}
print(dict)
for item in dict.items():
    print(item)
print("==")
for key in dict.keys():
    print(key)
print("==")
for value in dict.values():
    print(value)
print("==")
print(dict["hd"])
print(dict.get("sdf"))
del dict["hd"]
print("==")
print(dict)
dict["dsjlfd"] = "dsfdsfsdfd"
print(dict)
print("====pop===")
sd = dict.pop("sd")
print(dict)
print(sd)
dict["fsafe99"] = '123'
dict["bsafe99"] = '35'
dict["asafe99"] = '123'
for key, value in sorted(dict.items()):
    print("key :" + str(key) + ",value :" + str(value))
for value in sorted(set(dict.values())):
    print("value :" + str(value))
