# I normally use if/else statement in scripting to run pipelines or as a wrapper script

# A list is given with random orders
number = [5,4,1,2,32]

# Get the largest value from a list
print("Largest Digit: " + str(max(number)))
# Get the smallest value from a list
print("Smallest Digit: " + str(min(number)))

max_value = max(number)

if ( max_value > 50 ):
    print(" It exceeds our thresdhold! ")
else:
    print( "We are still Good! Ensure you have left about " + str(50-max_value) + " units! " )
