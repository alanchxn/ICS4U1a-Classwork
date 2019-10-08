# File --- RW
# 1. create the student list that is the list of dict, which has last, first name and assignment list (dict of  assignment) ---- same as first project
# 2. write def that can load this student list and save it as the json file
# 3  write def that read the json file to student list

# Dict --- Add/Remove/Edit by student or assignment

# Dict --- Top/Average/Sort by mark
import operator
import json
def json_list_save():
    studentlist = [
        {
            "first_name": "Evan",
            "last_name": "Chen",
            "classroom": "ICS",
            "assignments": [
                {
                "assignment_name": "markbook",
                "due_date": "9/25/2019",
                "mark": 97,
                }
            ]
        },
        {
            "first_name": "Alan",
            "last_name": "Chen",
            "classroom": "ICS",
            "assignments": [
                {
                "assignment_name": "markbook",
                "due_date": "9/25/2019",
                "mark": 99,
                }
            ]
        },
        {
            "first_name": "Daniel",
            "last_name": "Chen",
            "Classroom":"ICS",
            "assignments": [
                {
                "assignment_name": "markbook",
                "due_date": "9/27/2019",
                "mark": 87,
                }
            ]
        }
    ]
    with open('./proj_data.json', 'w') as fp:
        json.dump(studentlist, fp)

def new_addition_student(first_name: str, last_name: str, classroom: str, assignment: list ):
    ''' Adds a new student with an assigment to the file
    Args: 
        param1: first name as a string
        param2: last name as a string
        param3: classroom as a string
        param4: assignment as a list
    '''

    #add new student to dictionary
    # with open('proj_data.json', 'r') as fp:
    #     data = json.load(fp)
    #     new_d = {}
    #     new_d["first_name"] = first_name
    #     new_d["last_name"] = last_name
    #     new_d["class_room"] = classroom
    #     new_d["assignments"] = assignment
    #     data.append(new_d)

    #     # save to file
    #     with open('proj_data.json', 'w') as fp:
    #         json.dump(data, fp)


    #remove student based on the last name
    # with open('proj_data.json', 'r') as fp:
    #     data = json.load(fp)
    #     for i in data:
    #         if i["last_name"] == "Chen":
    #             data.remove(i)
                

    #     # save to file
    #     with open('proj_data.json', 'w') as fp:
    #         json.dump(data, fp)

    #edit specific mark based on the first name
    # with open('proj_data.json', 'r') as fp:
    #     data = json.load(fp)
    #     for i in data:
    #         if i["first_name"] == "Daniel":
    #             a_list = i["assignments"]
    #             for k in a_list:
    #                 if k["assignment_name"] == "markbook":
    #                     k["mark"] = 95
    #                     break

    #     # save to file
    #     with open('proj_data.json', 'w') as fp:
    #         json.dump(data, fp)

    #average of all assignments done by students
    # with open('proj_data.json', 'r') as fp:
    #     data = json.load(fp)
    #     sum = 0
    #     a_len = 0
    #     for i in data:
    #         a_list = i["assignments"]
    #         a_len = a_len + len(a_list)
    #         for k in a_list:
    #             sum = sum + k["mark"]
    #     print ("\n\nthe average the of the student's assignments is " + str(round(sum/a_len, 1)))            

    # print the highest mark within the students
    # with open('proj_data.json', 'r') as fp:
    #     data = json.load(fp)
    #     highest_value = 0
    #     for i in data:
    #         a_list = i["assignments"]
    #         for k in a_list:
    #             if k["mark"] > highest_value:
    #                 highest_value = k["mark"]
    #     print ("\n\nthe highest mark of the student's assignments is " + str(highest_value)) 

    #the order of the students sorted in alphabetical order
    # with open('proj_data.json', 'r') as fp:
    #     data = json.load(fp)
    #     sort_list = []
    #     for b in sorted(data, key=operator.itemgetter("first_name")):
    #         sort_list.append(b)
    #     print ("\n\nthe order of the students names in alphabetical order is " + str(sort_list)) 
    #     return sort_list  

    #sort the students in the dict based on an assignment mark
    with open('proj_data.json', 'r') as fp:
        data = json.load(fp)
        sort_list = []
        for b in data:
            new_dict = {}
            new_dict["first_name"] = b["first_name"]
            new_dict["last_name"]= b["last_name"]
            new_dict["mark"]= b["assignments"][0]["mark"]
            sort_list.append(new_dict)

        final_list = []
        for c in sorted(sort_list, key=operator.itemgetter("mark"), reverse=True):
            final_list.append(c)    
        print ("\n\nthe order of the students marks from highest to lowest is " + str(final_list)) 
        return sort_list  