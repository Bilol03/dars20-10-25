import json

# x = '{"ism": "Javlon", "yosh": 17}'
# print(x)

# x = json.loads(x)

# print(x)

# student = {
#     "ism": "Ulug'bek",
#     "yoshi": 14,
#     "sinf": 8,
#     "manzil": "parvoz ko'chasi"
# }
# print(type(student))

# student = json.dumps(student)

# print(type(student))

# print(json.dumps("string"))
# print(type(json.dumps(20)))
# print(json.dumps([21, 23, "stri"]))
# print(json.dumps(('data', 'data2')))
# print(20)

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(x)
# print(json.dumps(x))



student = {
    "ism": "Ismaloq",
    "age": 15,
    "school": {
        "name": 34,
        "location": "5/1a"
    },
    "sinf": 9,
    "manzil": {
        "davlat": "Uzbekistan",
        "city": "Olmaliq"
    }
}

student = json.dumps(student)
print(type(student))

student = json.loads(student)
print(type(student))
