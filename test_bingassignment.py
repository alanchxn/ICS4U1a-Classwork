import os.path
import json
def dict_test(): 
    import bingassignment
    bingassignment.json_list_save()
    expected = "[{'first_name': 'Alan', 'last_name': 'Chen', 'classroom': 'ICS', 'assignments': [{'assignment_name': 'markbook', 'due_date': '9/25/2019', 'mark': 91}]}, {'first_name': 'Daniel', 'last_name': 'Chen', 'Classroom': 'ICS', 'assignments': [{'assignment_name': 'markbook', 'due_date': '9/27/2019', 'assignment_mark': 87}]}]"
    if os.path.isfile("./proj_data.json"):
        with open('proj_data.json', 'r') as fp:
            result = json.load(fp)
            print("\n\n the result will be "+ str(result))
    assert expected == str(result)

def test_add():
    import bingassignment
    bingassignment.json_list_save()
    expected = "[{'first_name': 'Alan', 'last_name': 'Chen', 'classroom': 'ICS', 'assignments': [{'assignment_name': 'markbook', 'due_date': '9/25/2019', 'mark': 91}]}, {'first_name': 'Daniel', 'last_name': 'Chen', 'Classroom': 'ICS', 'assignments': [{'assignment_name': 'markbook', 'due_date': '9/27/2019', 'assignment_mark': 87}]}, {'first_name': 'Bing', 'last_name': 'Chen', 'class_room': 'Scotiabank', 'assignments': [{'assignment_name': 'Markbook', 'assignment_mark': '09/25/2002', 'mark': 79}]}]"
    assignments = [{"assignment_name": "Markbook", "due_date": "09/25/2002", "mark": 79 }] 
    bingassignment.new_addition_student("Bing", "Chen", "Scotiabank", assignments)
    # if os.path.isfile("./proj_data.json"):
    #     with open('proj_data.json', 'r') as fp:
    #         result = json.load(fp)
    #         print("\n\n the result will be "+ str(result))
    # assert expected == str(result)


def test_all():
    # dict_test()
    test_add()
    print("\n\n Passed all tests.")
test_all()
