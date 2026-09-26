dict1 = {
    "name": "John",
    "age": 25,
    "city": "Chennai"
}

dict2 = {
    "age": 30,
    "city": "Bangalore",
    "job": "Developer"
}

for key,value in dict1.items():

    for key1,value1 in dict2.items():

        if key == key1:

            print("Common keys",key)