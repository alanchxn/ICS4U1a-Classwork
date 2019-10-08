#printing different values/keys in dictionaries
student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11
}
for key in student.keys():
    print(key)
>>>first_name
>>>last_name
>>>grade
print()
for val in student.values():
    print(val)
>>>Frank
>>>Smith
>>>11
print()
for key, value in student.items():
    print(key, value)
>>>first_name: Frank
>>>last_name: Smith 
>>>grade: 11


#assign all values to "None" in a dictionary
student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}
for key in student.keys():
    student[key] = None
print(student)
>>>{'first_name': None, 'last_name': None, 'grade': None, 'homeroom': None}

#clear only certain values
student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}
for key in student.keys():
    if "name" in key:
        student[key] = None
print(student)
>>> {'first_name': None, 'last_name': None, 'grade': 11}