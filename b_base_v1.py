import pandas


# checks validity of user's number input according to
# set num_type in main routine. Takes in custom error message
def num_check(question, error, num_type):
    while True:

        try:
            # uses num_type and checks if user input is valid according
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that user has entered either yes or no
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


# function checks that the users input is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        # if the response is blank, outputs error
        if response == "":
            print("Sorry, this can't be blank or contain only spaces. Please try again.")
        else:
            return response


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# main routine goes here
get_int = num_check("How many do you need? ", "Please enter an integer more than 0\n", int)
get_cost = num_check("How much does it cost? $", "Please enter a number more than 0\n", float)
