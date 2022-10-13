# [1,2,9,12,23,30,50]
def KLargeest (arr,k):
    arr.sort(reverse = True)
    return arr[k-1]

def KSmallest (arr,k):
    arr.sort()
    return arr[k-1]
arr = [1,23,12,9,30,2,50]

# Get the 3rd largest value
print(KLargeest(arr,3))
# Get the 2nd smallest value
print(KSmallest(arr,2))
