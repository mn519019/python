# Wrtie a python program to count the frequency of words appearing in a string
# Example: Sheena loves eating apple and mango. Her sister also loves eating aplen and mango 

str1 = "Sheena loves eating apple and mango. Her sister also loves eating apple and mango"
x = str1.split(" ")

def frequent_word():
    duplicates=[]
    myfreq = [x.count(p) for p in x]
    return dict(zip(x,myfreq))

print(frequent_word())

## Output 
# {'Sheena': 1, 'loves': 2, 'eating': 2, 'apple' : 2, 'and': 2, 
# 'mango.': 1, 'Her': 1, 'sister': 1, 'also': 1, 'mango': 1}

# mylist = ["a", "b", "a", "c", "c"]
# myfreq = [mylist.count(p) for p in mylist]
# result = dict(zip(mylist,myfreq))
# print(result)