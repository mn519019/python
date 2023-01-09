# Find out pairs with given sum value of an array, Adopting a binary search approach and we can solve this question
# arr = [5,7,4,3,9,8,19,21] and sum= 17 

def find_target_sum(list,target):
    list.sort()
    print(list)
    left = 0
    right = len(list) -1
    
    for data in list:
        sum = list[left] + list[right]
        if sum > target:
            right = right - 1
        elif sum < target:
            left = left + 1
        elif sum == target:
            print("matching paris are: ",list[left],"&",list[right])
            left = left + 1
            right = right - 1
        else:
            print("no matching pairs are found to get ", target)  
    return " "


list1 = [0,5,7,4,3,9,8,21,19,17]
print(find_target_sum(list1,17))
