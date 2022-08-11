# Declare a fruit list 
random_fruits = ["blackberry", "apple", "mango", "strawberry", "banana"]
print("Original List:" + str(random_fruits))

# Insert a value into the lsit
random_fruits.insert(5, "grape")
#print(random_fruits)
print("After Insertion: " + str(random_fruits))

# Delete a value from the list
random_fruits.remove("grape")
print("After Deletion: " + str(random_fruits))

print("===================================== EOF =======================================")

# Get a length of the list
print("Total items in the lsit: " + str(len(random_fruits)))

print("===================================== EOF =======================================")
str_match = [s for s in random_fruits if "apple" in s]

if (str_match):
    print("Yes, it exists!")
else: 
    print("No, it's not there")
print("===================================== EOF =======================================")