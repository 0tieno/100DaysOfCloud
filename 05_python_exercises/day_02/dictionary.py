my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "status": "single",
    "children": 4
}

# ||METHODS OF RETRIEVING VALUES FROM A DICTIONARY - use key||
# print(my_dict["city"])
# print(my_dict.get("city"))

# ||FOR LOOP TO PRINT ALL KEYS/VALUES IN A DICTIONARY||
# for value in my_dict.values():
#     print(value)

# for key in my_dict.keys():
#     print(key)

for key, value in my_dict.items():
    print(key, value)
