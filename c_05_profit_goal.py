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


def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    while True:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or %)? ")

        # checks if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %...
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars?, (y / n): ")

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"

            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount}%, (y / n)? ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal
