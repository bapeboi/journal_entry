print("hello and welcome to your journaling app")
print("what would you like to do?")

print("choose from these three choices on what you'd like to do,[a]dd journal entry, [d]elete existing journal entry, "
      "[c]lose application.")

non_entry = "make existing entry"

while non_entry != selection:
    selection = input("what would you like to do:")
    if selection == "a":
        print(input("what would you like this journal entry to say?:"))

    elif selection == "d":
        print(input("which journal entry would you like to delete?:"))

    elif selection == "c":
        print("see you next time.")

