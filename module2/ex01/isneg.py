#!/usr/bin/env python3

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        number = int(user_input)
        if number == 0:
            print("This number is equal to zero")
        else:
            print("This number is different from zero")
    except ValueError:
        print("That's not a valid number. Please enter a valid integer.")