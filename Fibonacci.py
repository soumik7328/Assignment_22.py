#10. Write a recursive python function to find the Nth term of the Fibonacci series.
def Fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return Fibonacci(n-2) + Fibonacci(n-1)
    

print(Fibonacci(int(input("Enter which term of Fiibonacci series want see  "))))