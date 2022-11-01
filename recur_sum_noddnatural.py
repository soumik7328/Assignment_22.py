#2. Write a recursive python function to calculate sum of first N odd natural numbers

def odd(n):
    if n==1:
        return 1
    return (2*n-1 + odd((n-1)))

print(odd(int(input("\nEnter how many odd number's sum you want to print:-"))))