# This is a fizbuzz algorithm problem 
# Difficulty: Easy
# Qeustion: 
# Write a Python program which iterates the integers from 1 to n. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

# A Simple Version 

# Type your input to range from 1 to input n
n = int(input("Please type your input: "))

# for fizbuzz in range(1,n+1):
#    if fizbuzz % 3 == 0 and fizbuzz % 5 == 0:
#        print("FizBuzz")
#    elif fizbuzz % 3 == 0:
#        print("Fizz")
#    elif fizbuzz % 5 == 0:
#        print("Buzz")
#    else:
#        print(fizbuzz)

#  FizzBuzz With Using A List        


def fizzBuzz (n):
    l = []
    for x in range (1 , n+1):
        if x % 3 == 0 and x % 5 == 0:
            l.append("FizzBuzz")
        elif x % 3 == 0:
            l.append("Fizz")
        elif x % 5 == 0:
            l.append("Buzz")
        else:
            l.append(str(x))

        # Then print the list
    return l

# print(l)

def main():
    print(', '.join(fizzBuzz(n)))

main()

# https://leetcode.com/problems/k-diff-pairs-in-an-array/submissions/
