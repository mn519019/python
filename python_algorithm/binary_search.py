list1 = ['Alice','Kim','Bob','Corner','Minwoo','Domino','Elice','Frank'
        ,'Gong','Hay','Jason','Lion','Nan']

sortlist = sorted(list1)
print(sortlist)

# Binary Search Approach
def binary_search2(list,target):
    left = 0
    right = len(sortlist) - 1 
    while left<=right:
        mid = (left+right) // 2
        if target < list[mid]:
            right = mid -1
        elif target > list[mid]:
            left = mid + 1
        else:
            return list[mid] + " has been found on index " + str(mid)
    return ""


        
print(binary_search2(sortlist,'Kim'))

# Average Time complexity: O(logn)
# The best case: O(1)

# Linear Search Approach
# def linear_search(list,target):
#     for i, x in enumerate(list):
#         if x == target:
#             return str(x) +" has been found on index " + str(i)
#             break
        
# print(linear_search(sortlist,"Kim"))

