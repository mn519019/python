list1 = ['Alice','Kim','Bob','Corner','Minwoo','Domino','Elice','Frank'
,'Gong','Hay','Jason','Lion','Nan']

sortlist = sorted(list1)
# Binary Search Approach
def binary_search(list, target):
    left = 0
    right = len(list) -1 
    while(left<=right):
        mid = (left+right) // 2
        if list[mid] == target:
            return list[mid]
        elif list[mid] < target:
            left = mid + 1 
        else:
            right = mid -1
    return -1
        
print(binary_search(sortlist,'Kim'))

# Linear Search Approach
def linear_search(list,target):
    for i, x in enumerate(list):
        if x == target:
            return str(x) +" has been found on index " + str(i)
            break
        
print(linear_search(sortlist,"Kim"))

