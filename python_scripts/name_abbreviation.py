# Returns an abbreviated version of a full name.
# All names except the last are abbreviated with one letter.
# Example input 'Rick Minwoo Yang' should be 'Rick Minwoo Y'

def name_abbreviation(name):
    x = name.split()
    a = ""
    b = ""

    for i in range(0,len(x)-1):
        a = a+""+str(x[i]).upper()+" "
        for j in range(len(x)-1, len(x)):
            b = "."+str(x[j][0]).upper()
    return a + b


# Test Case
# Expectation: Rick Minwoo .Y
print(name_abbreviation('Rick Minwoo Yang')) 
# Expectation: Hailey Jo
print(name_abbreviation('Hailey Jo'))
# Expectation: Eric He Nice Man
print(name_abbreviation('Eric He Nice Man')) 
