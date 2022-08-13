# Search x in arr[]
# If x is present then return its location, otherwise print "N/A"
# Difficulty: Easy
# Disadvantage: It's slower than other search algorithms such as binary or hash tables. 
# However, it gives us basic understanding how a search algorithm would work 

# l: list
# n: number of elements in an array
# x: number to be found

x = int(input("Please type a number you want to find "))

# Declare an array
l = [1,2,3,4,5,6,7,8,9,10]
n   = len(l)

def linear_search(l,x):
    for i in range(len(l)):
        if (l[i] == x):
            return True        
    return False

search = linear_search(l,x)
print("search value: ", search)

if (search == False):
    print(str(x) + " is not available in a list ")
else:
    print(str(x) + " has found in a list at " + str(l.index(x)))
