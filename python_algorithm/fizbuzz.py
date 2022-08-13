# This is a fizbuzz algorithm problem 
# Difficulty: Easy
# Qeustion: 
# Write a Python program which iterates the integers from 1 to n. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

n = int(input("Please type your input: "))

for fizbuzz in range(1,n+1):
    if fizbuzz % 3 == 0 and fizbuzz % 5 == 0:
        print("FizBuzz")
    elif fizbuzz % 3 == 0:
        print("Fizz")
    elif fizbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizbuzz)
