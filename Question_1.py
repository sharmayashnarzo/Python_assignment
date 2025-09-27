"""Take 2 numbers as input (X and Y) and a third number N.
 Display all the numbers between X and Y 
(X < i <= Y) that are divisible by N.
"""
X = int(input("Enter the value X : "))
Y = int(input("Enter the value Y : "))
N = int(input("Enter the value N : "))

for i in range(X, Y):
    if(i%N == 0):
        print(i , " is divisible by " , N)