def missing_number(list):
    sortlist = sorted(list)
    biggest = sortlist[len(sortlist)-1]
    for i in range(0,biggest+1):
            if i not in sortlist:
                return i
                break
    return biggest+1

# Driver Code     
if __name__ == "__main__" :
    list1 = [3,0,1]
    list2 = [0,1]
    list3 = [9,6,4,2,3,5,7,0,1]
    print(missing_number(list1)) # Expect 2 
    print(missing_number(list2)) # Expect 2
    print(missing_number(list3))  # Expect 8
