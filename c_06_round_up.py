import math


# rounding function - rounds to nearest 'round_to' value.
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# Main routine
to_round = [2.65, 2.25, 2]
for item in to_round:
    rounded = round_up(item, 1)
    print(f"${item:.2f} --> ${rounded:.2f}")
