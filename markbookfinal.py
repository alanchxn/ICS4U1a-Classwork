import json
import operator
import os.path


def main():

    if os.path.isfile("./proj_data.json"):
        with open('proj_data.json', 'r') as fp:
            data = json.load(fp)
    else:
        # analysis data
        data = [
                    {
                        "last_name": "chen",
                        "first_name": "alan",
                        "class_room": "ICS4U",
                        "assignments": [
                            {
                                "assignment_name": "project_1",
                                "due_date": "2019/09/30",
                                "mark": 95,
                            },
                            {
                                "assignment_name": "project_2",
                                "due_date": "2019/09/30",
                                "mark": 97,
                            }
                        ]
                    },
                    {
                        "last_name": "berry",
                        "first_name": "max",
                        "class_room": "ICS4U",
                        "assignments": [
                            {
                                "assignment_name": "project_1",
                                "due_date": "2019/09/30",
                                "mark": 62,
                            },
                            {
                                "assignment_name": "project_2",
                                "due_date": "2019/09/30",
                                "mark": 70,
                            }
                        ]
                    }
            ]
        # save data into proj_data.json
        with open('./proj_data.json', 'w') as fp:
            json.dump(data, fp)
    # menu while loop
    while exit != "yes":
        print("_" * 50)
        print("0 - Exit")
        print("1 - Add/Remove/Edit Student")
        print("2 - Add/Remove/Edit Assignment(Mark)")
        print("3 - Display the average")
        print("4 - Marks lower than 65")
        print("5 - Display top mark")
        print("6 - Class report")
        print("_" * 50)
        option = int(input("What would you like to do? "))

        if option == 0:
            break

        if option == 1:

            action = input("Would you like to add, remove, or edit students? ")

            if action == "add":
                f_name = input("first_name: ")
                l_name = input("last_name: ")
                c_room = input("class_room: ")

                new_d = {}
                new_d["first_name"] = f_name
                new_d["last_name"] = l_name
                new_d["class_room"] = c_room
                data.append(new_d)

                # save to file
                with open('proj_data.json', 'w') as fp:
                    json.dump(data, fp)
            elif action == "remove":
                f_name = input("what's your first_name: ")
                # remove person based on first name
                with open('proj_data.json', 'r') as fp:
                    data = json.load(fp)
                    for l in data:
                        if f_name == l["first_name"]:
                            data.remove(l)
                            break
                # save to file
                with open('proj_data.json', 'w') as fp:
                    json.dump(data, fp)

            elif action == "edit":
                # edit person based on first name
                f_name = input("What is your first_name: ")
                with open('proj_data.json', 'r') as fp:
                    data = json.load(fp)
                    for l in data:
                        if f_name == l["first_name"]:
                            f_name = input("new first_name: ")
                            l_name = input("new last_name: ")
                            c_room = input("new class_room: ")
                            l["first_name"] = f_name
                            l["last_name"] = l_name
                            l["class_room"] = c_room
                            break
                # save to file
                with open('proj_data.json', 'w') as fp:
                    json.dump(data, fp)

        if option == 2:
            action = input("Would you like to add, remove, or edit assignments? ")
            if action == "add":
                f_name = input("What is your first_name: ")
                # add it based on first name
                with open('proj_data.json', 'r') as fp:
                    data = json.load(fp)
                    for l in data:
                        if f_name == l["first_name"]:
                            assig_d = {}
                            assig_d["assignment_name"] = input("new assignment name : ")
                            assig_d["due_date"] = input("new due_date : ")
                            assig_d["mark"] = input("new mark : ")
                            assig_l = []
                            assig_l.append(assig_d)
                            l["assignments"] = assig_l
                # save to file
                with open('proj_data.json', 'w') as fp:
                    json.dump(data, fp)
            elif action == "remove":
                f_name = input("What is your first_name: ")
                # remove it based on first name and assignment name
                with open('proj_data.json', 'r') as fp:
                    data = json.load(fp)
                    for l in data:
                        if f_name == l["first_name"]:
                            a_name = input("What is your assignment name: ")
                            l["assignments"].remove(a_name)
                # save to file
                with open('proj_data.json', 'w') as fp:
                    json.dump(data, fp)
            elif action == "edit":
                f_name = input("what's your first_name: ")
                a_name = input("what's your assignment name: ")
                # edit it based on first name and assignment name
                with open('proj_data.json', 'r') as fp:
                    data = json.load(fp)
                    for l in data:
                        if f_name == l["first_name"]:
                            for assig_d in l["assignments"]:
                                if a_name == assig_d["assignment_name"]:
                                    assig_d["assignment_name"] = input("new assignment name: ")
                                    assig_d["due_date"] = input("new due_date: ")
                                    assig_d["mark"] = input("new mark: ")

                # save to file
                with open('proj_data.json', 'w') as fp:
                    json.dump(data, fp)
                break

        if option == 3:
            print ("\n\nDisplay the average: ")
            with open('proj_data.json', 'r') as fp:
                data = json.load(fp)

                for l in data:
                    f_name = l["first_name"]
                    s_total = 0
                    if "assignments" in l:
                        for assigment in l["assignments"]:
                            s_total = s_total + int(assigment["mark"])
                        s_average = float(s_total) / len(l["assignments"])
                        print ("\n Student: " + f_name + " average of all assignments: " + str(s_average) + "\n")
        if option == 4:
            print ("\n\nMarks lower than 65: ")
            with open('proj_data.json', 'r') as fp:
                data = json.load(fp)
                lower_mark = 65
                for l in data:
                    f_name = l["first_name"]
                    if "assignments" in l:
                        for assigment in l["assignments"]:
                            a_name = assigment["assignment_name"]
                            av = int(assigment["mark"])
                            if av <= lower_mark:
                                print ("\n" + f_name + " " + a_name + " mark: " + str(av) + "\n\n")

        if option == 5:
            print ("\n\nDisplay top mark: \n")
            with open('proj_data.json', 'r') as fp:
                data = json.load(fp)
                top_mark = 0
                top_l_name = ""
                top_a_name = ""
                for l in data:
                    f_name = l["first_name"]
                    if "assignments" in l:
                        for assigment in l["assignments"]:
                            a_name = assigment["assignment_name"]
                            av = int(assigment["mark"])
                            if av >= top_mark:
                                top_mark = av
                                top_l_name = f_name
                                top_a_name = a_name
                print ("\n" + top_l_name + " " + top_a_name + " mark: " + str(top_mark) + "\n\n")
        if option == 6:
            with open('proj_data.json', 'r') as fp:
                data = json.load(fp)
                goodprint = json.dumps(data, indent=4)
                print ("\n\Data : \n" + goodprint)

            print ("\nClass assignment marks (mark for each student's assignments): \n")

            print ("Class order by first name alpha : \n")
            with open('proj_data.json', 'r') as fp:
                data = json.load(fp)
                c_average = 0
                total_s_average = 0
                mark_order_list = []

                for l in sorted(data, key=operator.itemgetter("first_name")):
                    f_name = l["first_name"]
                    l_name = l["last_name"]
                    print ("\n" + f_name + "," + l_name + " : ")
                    s_total = 0
                    if "assignments" in l:

                        for assigment in l["assignments"]:
                            a_name = assigment["assignment_name"]
                            a_mark = assigment["mark"]
                            s_total = s_total + int(a_mark)
                            print ("\t" + a_name + " : " + str(a_mark))

                        s_average = float(s_total) / len(l["assignments"])
                        print ("\taverage : " + str(s_average))
                        total_s_average = total_s_average + s_average

                        mark_order_dict = {}
                        mark_order_dict["first_name"] = f_name
                        mark_order_dict["last_name"] = l_name
                        mark_order_dict["average"] = s_average
                        mark_order_list.append(mark_order_dict)

                c_average = float(total_s_average) / len(data)
                print ("\nclass average : " + str(round(c_average, 2)) + "\n\n")

                print ("\nClass order by student's average mark : \n")
                for n in sorted(mark_order_list, key=operator.itemgetter("average"), reverse=True):
                    a = n["average"]
                    l = n["last_name"]
                    f = n["first_name"]
                    print (str(a) + " : " + f + "," + l + "\n")
                print ("\n\n")


if __name__ == "__main__":
    main()
