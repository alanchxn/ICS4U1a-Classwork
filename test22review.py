#printing different values/keys in dictionaries
student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11
}
print("\n\ndict() students :\n" + str(student))

print("\n\nkeys() in a dictionary")
for key in student.keys():
    print(key)
# >>>first_name
# >>>last_name
# >>>grade


print("\n\nvalues() in a dictionary")
for val in student.values():
    print(val)
# >>>Frank
# >>>Smith
# >>>11

print("\n\nitems() in a dictionary")
for key, value in student.items():
    print(key, value)
# >>>first_name: Frank
# >>>last_name: Smith 
# >>>grade: 11


print("\n\nassign all values to None in a dictionary")
student = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}
for key in student.keys():
    student[key] = None
print(student)
# >>>{'first_name': None, 'last_name': None, 'grade': None, 'homeroom': None}

print("\n\nclear only certain values")
student4 = {
    "first_name": "Frank",
    "last_name": "Smith",
    "grade": 11,
    "homeroom": "11G"
}
for key in student4.keys():
    if "name" in key:
        student4[key] = None

print(student4)
# clear only certain values
# {'first_name': None, 'last_name': None, 'grade': 11, 'homeroom': '11G'}

print("\n\nget-a-list-of-keys-with-a-certain-value")
fruit = {
    "apples": 5,
    "pears": 2,
    "plums": 11,
    "peaches": 7
}

shopping_list = []
for fruit, qty in fruit.items():
    if qty <= 5:
        shopping_list.append(fruit)

print(shopping_list)
# get-a-list-of-keys-with-a-certain-value
# >>>['apples', 'pears']

student_final_marks = {
    "bing": 60,
    "daniel": 90,
    "alan": 95
}
def student_avg(marks:dict) -> return_float:
    """Calculate the average of students' marks

    Args:
        param1: students final marks by dictionary
    Returns:
        The average of the students' marks rounded to 1 decimal place
    """
    result = sum(marks.values()) / len (marks)
    return round(result, 1)

def test_avg(students: dict):
    expected = 81.7

    result = student_avg(student_final_marks)
    print("\nthe result of student_avg :" + str(result))
    assert expected == result

test_avg(student_final_marks)


