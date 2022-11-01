#5. Write a recursive python function to calculate sum of cubes of first N natural numbers
def square(n):
    if n==1:
        return 1
    return n**3 + square(n-1)

print(square(int(input("enter how many number's cube sum want to print?"))))