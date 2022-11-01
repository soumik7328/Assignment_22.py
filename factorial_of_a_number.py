#6. Write a recursive python function to calculate the factorial of a number.
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(factorial(int(input("Enter a number, to get factorial= "))))