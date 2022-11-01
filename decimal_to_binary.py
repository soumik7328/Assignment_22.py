#8. Write a recursive python function to print binary of a given decimal number.

def abc(n):
    if (n > 0):
        abc(int(n/2))
        print(n%2, end='')


abc(int(input("Enter a decimal number to get binary=")))
