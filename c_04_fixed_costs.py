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
def not_blank(question, error):
    while True:
        response = input(question).strip()

        # if the response is blank, outputs error
        if response == "":
            print(f"\n {error}. Please try again.\n")
        else:
            return response


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# gets expenses, returns list which has
# the data frame and subtotal
def get_expenses(var_fixed):
    # setup dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name , quantity and item
        item_name = not_blank("Item name: ", "The item name cannot be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero.", int)

        else:
            quantity = 1
        
        price = num_check("How much for a single item? $", "The price must be a number (more than 0)", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # calculate Cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # find subtotal
    sub_total = expense_frame['Cost'].sum()

    # currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# *** main routine starts here ***

# Get user data
# product_name = not_blank("Product name: ", "The product name cannot be blank.")

fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]


# printing area
print()
print(fixed_frame[['Cost']])
print()

print(f"Fixed Costs: ${fixed_sub:.2f}")
