import math


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


# rounding function - rounds to nearest 'round_to' value.
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# Main routine starts here
how_many = num_check("How many items? ", "Can't be 0", int)
total = num_check("Total Costs? ", "More than 0", float)
profit_goal = num_check("Profit Goal? ", "More than 0", float)
amount_round = num_check("Round to nearest...? ", "Can't be 0", int)

sales_needed = total + profit_goal

print(f"Total: ${total:.2f}")
print(f"Profit Goal: ${profit_goal:.2f}")

selling_price = sales_needed / how_many
print(f"Selling Price (not rounded): ${selling_price:.2f}")

recommended_price = round_up(selling_price, amount_round)
print(f"Recommended Price: ${recommended_price:.2f}")
