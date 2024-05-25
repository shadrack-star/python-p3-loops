#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    # Print the final message
    print("Happy New Year!")

def square_integers(int_list):
    # Initialize an empty list to store the squared integers
    squared_integers = []
     # Loop through each integer in the input list
    for i in int_list:
        # Square the integer and add it to the squared_integers list
        squared_integers.append(i ** 2)
    # Return the list of squared integers
    return squared_integers

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
     