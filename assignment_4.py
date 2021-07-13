# import is_field_blank from asgn4_Gui_module
# import is_field_a_number from asgn4_Gui_module

from asgn4_Gui_module import is_field_blank
from asgn4_Gui_module import is_field_a_number


# Defining main function
def main():
    print("Assignment 4")
    first_name = input("What is your first name?")
    # call is_field_blank function
    # checks whether the first name is blank
    while is_field_blank(first_name):
        print("First Name must be Entered")
        first_name = input("What is your first name?")

    last_name = input("What is your last name?")
    # call is_field_blank function
    # checks whether the last name is blank
    while is_field_blank(last_name):
        print("Last Name must be Entered")
        last_name = input("What is your last name?")

    age = ''
    age = input("What is your age?")
    if age == '':
        print("Age must be Entered")
    # call is_field_a_number function
    # checks whether age is blank
    while is_field_a_number(age):
        print("Age must be a Number")
        age = input("What is your age?")

    # checks if the user's age is over 40 display a message
    if age > '40':
        print("Well", first_name, last_name, " it looks like you are over the hill")
    else:
        print("It looks like you have many programming years ahead of you", first_name, last_name)

    print("END OF ASSIGNMENT 4")
# __name__
if __name__ == "__main__":
    main()
