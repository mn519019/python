import math

# method1
# Assign values for a digit to be powered
num   = 3 
power = 4
# There are few ways to power a given digit 
print("3^4 = " + str(math.pow(num,power)))


# method2 
# Creating a function 
def power(n,e):
    if e==0:
        return 1
    elif e==1:
        return n
    else:
        return math.pow(n,e)

n = 4
e = 3
print("4^3 = "+ str(power(4,3)))
