#9. Write a recursive python function to print octal of a given decimal number
def DecimalToOctal(n):
    if(n > 0):
        # recursively calling on n/8    
        DecimalToOctal(int(n/8))
        # printing the remainder
        #print(n)
        print(n%8, end='')
        
DecimalToOctal(int(input("Enter a decimal number to get octal number=")))