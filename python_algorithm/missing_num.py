# Find missing number in an array using sumation and XOR operation

def find_num(arr):
    length= len(arr) -1
    i = arr[length]
    j = arr[length]+1
    sum = 0
    if arr:
        num = (i*j)/2
        for data in arr:
             sum+=data
        calc = num-sum
        return calc
    else:
        print("An array is not provided.")
        return False

list1 = [1,2,3,4,5,7]
print(find_num(list1))