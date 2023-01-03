# Wrtie a Python Program to find out common leters between two strings 
# EX: NAINA && RENEE
# A common letter is N 

str1 = set('NAINA')
str2 = set('RENEE')

def check():
    if not str1 and str2:
        print("Value is null.") 
    for i in str1:
        for j in str2:
            if i == j:
                print("Identical letter has found: " + j)
                break

# Call a method            
check()