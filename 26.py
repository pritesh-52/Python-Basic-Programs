#find the HCF

# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:  #56
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input("Enter Number 1"))
num2 =int(input("Enter Number 2"))

print("The H.C.F. is", compute_hcf(num1, num2))



def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = 36
num2 = 48
hcf = find_hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is", hcf)


