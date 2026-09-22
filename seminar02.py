"""
Do this now - write a small program to determine
the % of students who have done Online Test 1.
(17 of 68 students)
"""

import random

# number_of_students_completed = 17
# number_of_students_total = 68
# print(f"Percentage: {number_of_students_completed / number_of_students_total :.2%}")

# Warmup question
# Write a program that asks the user for a low and high number, ensuring the high is higher than the low.
# Then print n smiley faces :slightly_smiling_face: where n is a random number betw

low = int(input("Low: "))
high = int(input("High: "))
while low >= high:
    print("Error")
    high = int(input("High: "))
print(random.randint(low, high) * ":)")
