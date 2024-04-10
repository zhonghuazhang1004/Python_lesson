

database = {
    "students": [
        {"first_name": "John", "last_name": "Smith", "class": "3C"},
        {"first_name": "Anna", "last_name": "Purple", "class": "3C"},
        {"first_name": "Jan", "last_name": "Kowalski", "class": "4E"},
    ],
    "teachers": [
        {"first_name": "John", "last_name": "Hady", "subject": "math", "classes_taught": ["3C", "4E"]},
    ],
    "homeroom_teachers": [
        {"first_name": "Jan", "last_name": "Kowalski", "class": "3C"},
    ]
}


def show_database_info(database):
    for user_type, users in database.items():
        print(f"{user_type.capitalize()}:")
        if len(users) == 0:
            print("  No users found")
        else:
            for user in users:
                print("  -", end=" ")
                for key, value in user.items():
                    if isinstance(value, list):
                        value = ", ".join(value)
                    print(f"{key.capitalize()}: {value}", end=", ")
                print()


def display_command():
    list = ["1.create", "2.manage", "3.end"]
    print("------welcome------")
    for command in list:
        print(command)


def create_user():
    while True:
        createList = ["1.student", "2.teacher", "3.homeroom teacher", "4.end"]
        print("----------Create Function----------")
        for command in createList:
            print(command)

        user_type = input("Please enter your choice:")
        # - 'student': Prompt for the student's first and last name (as one or two variables,
        # depending on your design) and the class name (e.g., "3C").
        if user_type == "1":
            first_name = input("First student's name:")
            last_name = input("Last student's name:")
            class_name = input("Class name:")
            #     student infor storage
            database["students"].append({"first_name": first_name, "last_name": last_name, "class": class_name})

            # - 'teacher': Prompt for the teacher's first and last name (as one or two variables, depending on your
            # design), the subject they teach, and the names of the classes they teach, until an empty line is entered.
        elif user_type == "2":
            print("*****please enter teacher's information*****")
            first_name = input("First teacher's name:")
            last_name = input("Last teacher's name:")
            subject = input("Subject:")

            class_taught = []
            # taught subject storage
            while True:
                class_name = input("Enter class name they teach (or enter nothing to finish):")
                if class_name == "":
                    break
                else:
                    class_taught.append(class_name)

            # teacher information storage

            database["teachers"][f"{first_name} {last_name}"] = {"first_name": first_name, "last_name": last_name,
                                                                 "subject": subject, "classes_taught": class_taught}

        # - 'homeroom teacher': Prompt for the homeroom teacher's first and last name (as one or two variables,
        # depending on your design), and the name of the class they lead.
        elif user_type == "3":
            first_name = input("First homeroom teacher's name:")
            last_name = input("Last homeroom teacher's name:")
            lead_class = input("Name of the class they lead:")
            database['homeroom_teachers'].append(
                {'first_name': first_name, 'last_name': last_name, 'class_led': lead_class})
        elif user_type == "4":
            break
        else:
            print("Invalid Command")


def manage_user():
    # Prompt for an option to manage: class, student, teacher, homeroom teacher, end. After managing an option (
    # except for 'end'), the menu should be displayed again.
    manageList = ["1.class", "2.student", "3.teacher", "4.homeroom teacher", "5.end"]
    print("----------Manage Function----------")
    for command in manageList:
        print(command)
    choice = input("Please enter your choice:")
    # 'class': Prompt for a class to display (e.g., "3C"), the program should list all students in the class
    # and the homeroom teacher.
    if choice == "1":
        class_name = input("enter class name to display:")

        print(f"\nStudents in class {class_name}:")
        for student in database['students']:
            if student['class'] == class_name:
                print(f"{student['first_name']} {student['last_name']}")

        print(f"\nHomeroom teacher of class {class_name}:")
        for teacher in database['homeroom_teachers']:
            if teacher['class_led'] == class_name:
                print(f"{teacher['first_name']} {teacher['last_name']}")

    # 'student': Prompt for a student's first and last name,
    # the program should list all the classes the student attends and
    # the teachers of these classes.
    elif choice == "2":
        student_first_name = input("enter student's first name:")
        student_last_name = input("enter student's last name:")
        found = False
        for student in database["students"]:
            if student["first_name"] == student_first_name and student["last_name"] == student_last_name:
                # list all the classes the student attends
                print(
                    f"classes attended by student : {student['first_name']} {student['last_name']} : {student['class']}")
                for teacher in database["teachers"]:
                    if student["class"] in teacher["classes_taught"]:
                        print(f"taught teacher is {teacher['first_name']} . {teacher['last_name']}")
                        found = True
        if not found:
            print("Student not found")

    # 'teacher': Prompt for a teacher's first and last name,
    # the program should list all the classes the teacher teaches.
    elif choice == "3":
        teacher_first_name = input("enter teacher's first name:")
        teacher_last_name = input("enter teacher's last name:")
        found = False
        for teacher in database["teachers"]:
            if teacher["first_name"] == teacher_first_name and teacher["last_name"] == teacher_last_name:
                print(f"classes taught by {teacher['first_name']}{teacher['last_name']}")
                for classes in teacher['classes_taught']:
                    print(f"{classes}")
                found = True
        if not found:
            print("teacher not  found!")

            # 'homeroom teacher': Prompt for a homeroom teacher's first and last name,
            # the program should list all students the homeroom teacher leads.
    elif choice == "4":
        hometeacher_first_name = input("enter home teacher's first name:")
        hometeacher_last_name = input("enter home teacher's last name:")
        found = False
        for hometeacher in database['homeroom_teachers']:
            if hometeacher['first_name'] == hometeacher_first_name and hometeacher[
                'last_name'] == hometeacher_last_name:
                print(f"\nStudents led by {hometeacher['first_name']} {hometeacher['last_name']}:")
                for student in database['students']:
                    if student['class'] == hometeacher['class']:
                        print(f"- {student['first_name']} {student['last_name']}")
                    found = True
        if not found:
            print("Homeroom teacher not found")


def main():
    while True:
        display_command()
        command = input("enter your command:")
        #create
        if command == '1':
            create_user()
        #manage
        elif command == '2':
            manage_user()
        #end
        elif command == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid command")



if __name__ == "__main__":
    main()