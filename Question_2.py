""" 
Take a positive integer as input and display the sum of its digits.
The number can be of any length.
"""

variable1 = int(input("Enter a positive integer : "))
if variable1 < 10:
    print("Please enter atlest 2 digit number")
    exit()
temp = variable1
remainder = int()
sum = int()
while variable1 > 0:
    remainder = variable1 % 10 
    sum = sum + remainder
    variable1 = variable1 // 10
print("Sum of the digits of number ",temp, " is ", sum)