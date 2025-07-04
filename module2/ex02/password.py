#!/usr/bin/env python3
password = input("Enter a password please:")

if password.strip().lower() == "python is awesome".lower():
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")       