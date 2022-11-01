#3. Write a recursive python function to calculate sum of first N even natural numbers
def even(n):
    if n==1:
        return 2
    return n*2 + even(n-1)
        #print(n+((n*2)),end=' ')

print(even(int(input("\nEnter how many even number's sum you want to print:-"))))