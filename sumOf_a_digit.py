#7. Write a recursive python function to calculate sum of the digits of a given number
def sum_numberr(n):
    if n>0:
        return n%10 +sum_numberr(int(n//10))

    return n

print(sum_numberr(int(input("Enter a digit. To get the digit sum="))))
