def yes_no(question):
    yes_no_list = ['yes', 'no']

    # error code
    error = f"Please choose either '{yes_no_list[0]}' or '{yes_no_list[1]}'."

    while True:
        # Ask the user if they have played before
        print("")
        response = input(question).lower()

        # If they say yes, output 'program continues'
        for item in yes_no_list:
            if response == item[:1] or response == item:
                return item

        # output error if item not in list, checks item if it is in yes_no_list, then continues to this.
        print(f"{error}\n")


for i in range(0, 5):
    wait_instructions = yes_no("Do you want to read the instructions (y/n): ")
    print(f"You chose {wait_instructions}")
