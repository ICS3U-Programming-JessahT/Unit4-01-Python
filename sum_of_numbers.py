#!/usr/bin/env python3

# Created By: Jessah
# Date: Nov 8, 2022
# This program ask the user for a positive integer and it will track the loop.


def main():
    # set sum and counter to zero
    loop_counter = 0
    sum = 0
    # get input from user
    user_string = input("Enter a positive number: ")
    # catch any invalid inputs
    try:
        user_integer = int(user_string)

    except Exception:
        print("")
        print("Enter a positive integer")
        print("{} is not a valid input".format(user_string))
    # if input is an integer it goes to else
    else:
        if user_integer >= 0:  # It will only continue if the user a # >= 0

            while loop_counter <= user_integer:
                sum = sum + loop_counter
                print("Tracking {0} number in the loop".format(loop_counter))
                loop_counter = loop_counter + 1

            print("")
            print("The sum of the numbers is {}".format(sum))

        else:
            print("")
            print("{} is not a valid input,".format(user_integer))
            print("enter a positive integer")


if __name__ == "__main__":
    main()
