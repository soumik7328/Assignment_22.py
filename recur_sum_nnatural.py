#1. Write a recursive python function to calculate sum of first N natural numbers
def  sum_natural_num(n):
    if n==1:
        return 1
    return n + sum_natural_num(n-1)

n=int(input("Enter how many number's sum want to print?"))
print(sum_natural_num(n))

