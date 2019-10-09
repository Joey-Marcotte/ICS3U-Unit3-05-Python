#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program finds the month of a number


def main():
    # this function finds the month of a number
    while True:
        # input
        number_of_month = int(input("Enter a number of a month(1-12): "))

        # process and output
        if number_of_month == 1:
            print("January")
            break
        elif number_of_month == 2:
            print("February")
            break
        elif number_of_month == 3:
            print("March")
            break
        elif number_of_month == 4:
            print("April")
            break
        elif number_of_month == 5:
            print("May")
            break
        elif number_of_month == 6:
            print("June")
            break
        elif number_of_month == 7:
            print("July")
            break
        elif number_of_month == 8:
            print("August")
            break
        elif number_of_month == 9:
            print("September")
            break
        elif number_of_month == 10:
            print("October")
            break
        elif number_of_month == 11:
            print("November")
            break
        elif number_of_month == 12:
            print("December")
            break
        else:
            print("Not a month")


if __name__ == "__main__":
    main()
