# Find minimum difference betwween two elements of array
# arr = [5,32,45,4,12,18,25]

def find_min_diff(list):
    list.sort()
    diff = 99999*999
    print(list)
    for i in range(len(list)-1):
        if list[i+1]-list[i] < diff:
            diff = list[i+1]-list[i]
            print("First element: " + str(list[i]) + " Second Element: " + str(list[i+1]))
        return diff


list1 = [1,5,19,10,9,13]
print("Minimum Diff is ",find_min_diff(list1))