import random

meatList = ["Fish", "Shrim", "Shell"]

detect = "y"

while True:
    if detect == "y":
        select = random.choice(meatList)
        print("I want: ", select)
        # detect = input("again ? (y yes n no):")
        detect = "n"
    else:
        break
