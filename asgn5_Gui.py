import random

print("assignment 5",sep="\n\n")
my_classes = ['Python', 'Javascript', 'Php']


def displayMyClasses():
    my_classes.sort()
    print("List of Classes I Teach:")
    for (i, item) in enumerate(my_classes, start=1):
        print(i, item)
    # print(*my_classes, sep="\n")


def guessNext():
    rad = random.choice(my_classes)
    print("The next class you should teach is:", rad)


def addClass():
    class_add = input("Enter the name of the class you wish to add: ")
    my_classes.append(class_add)


def removeClass():
    class_rm = input("Enter the name of the class you wish to remove: ")
    my_classes.remove(class_rm)


def main():
    displayMyClasses()
    done = False
    while not done:
        choice = input("Do you need to Add or Remove a class? (A/R): ")
        if choice == "A" or choice == "a":
            addClass()
        else:
            print("You must choose an 'A' to Add or an 'R' to Remove a class")
        if choice == 'R' or choice == "r":
            removeClass()
        if repr(choice) == repr(''):
            break

    displayMyClasses()
    guessNext()
    print("END OF ASSIGNMENT 5")


# __name__
if __name__ == "__main__":
    main()
