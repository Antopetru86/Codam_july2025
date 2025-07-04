#!/usr/bin/env python3
print("Enter a number")
num1 = int(input())
num_hold= 0

while num_hold<11:
    new_num = num1 *num_hold
    print(f"{num1}*{num_hold} = {new_num}")
    num_hold += 1

