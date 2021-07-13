print("Assignment 3")
your_name = input("What is your name?")
# print(your_name)
print("Please Enter the names of your three best friend")
friends = []
for x in range(3):
    friend = input("Enter Friend Name:")
    friends.append(friend)
print("My Best Friends are:")
for (i, item) in enumerate(friends, start=1):
    print(i, item)

print("Now enter the names of other people you are inviting to your wedding")
guests = []
done = False
while not done:
    guest = input("Guest's Name (or press Enter to quit:)")
    guests.append(guest)
    if repr(guest) == repr(''):
        break
print("My Wedding Attendees are:")
for (i, item) in enumerate(guests, start=1):
    print(i, item)
print("END OF ASSIGNMENT 3")
