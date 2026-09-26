dict1 = {
    "name": "John",
    "age": 25
}

dict2 = {
    "city": "Chennai",
    "job": "Developer"
}

for key,value in dict2.items():

    dict1[key] = value

print("the dict1",dict1)