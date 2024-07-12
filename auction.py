import os
from logo import logo


print(logo)
print("Welcome to the secret auction program.")
all_bidders = {}
flag = True

while flag:
    names = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if other_bidders == 'yes':
        all_bidders.update({names:bid})
        os.system('cls')  # cleans the screen if you run the program in the terminal, it cleans the screen so that the other
                          # bidders do not know how much you bid
        flag = True
    elif other_bidders == 'no':
        flag = False
        top_b = max(all_bidders, key=all_bidders.get)
        print(f'The top bidder is {top_b}, with a bid of ${bid}')