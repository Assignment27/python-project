# Exercise 1: Student Course Registration System
# Create a program that:
#
# Stores available courses in a dictionary where:
# Key = course code
# Value = course name

# Allows students to register courses.
# Prevents duplicate course registrations using a set.
# Uses a while loop to keep displaying a menu. --
# Uses a match statement for menu navigation. --
# Stores registered courses in a list.
# Display all registered courses using a for loop.
# Stores student information in a tuple (student_id, name).

courses = {
    "web101" : "Web Development",
    "cyber404" : "Cyber-Security",
    "data213" : "Data Analyst",
    "ful101" : "Full-Stack Development"
}


def display_courses():
    print("Available courses:")
    for i in courses:
        print(i, ":", courses[i])

def register_courses():
    print("course Registration")
    count = 0
    for i in courses:
        count += 1
        print(f"{count}. {i} : {courses[i]}")
    option = input("select  course to register:")

register_courses()



