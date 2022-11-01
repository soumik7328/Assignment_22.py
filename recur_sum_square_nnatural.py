#4. Write a recursive python function to calculate sum of squares of first N natural numbers
def square(n):
    if n==1:
        return 1
    return n**2 + square(n-1)

print(square(int(input("enter how many number's square sum want to print?"))))