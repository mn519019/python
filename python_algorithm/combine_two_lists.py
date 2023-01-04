l1=["Nina","Kim","Lee"]
l2=[133,157,159]

def combine_lists(list1,list2):
    l3 = dict(zip(l1,l2))
    return l3

print("Dictionary: \n", combine_lists(l1,l2))

def convert_tuple():
    print("\nTuples:")
    dict1 = combine_lists(l1,l2)
    for i in dict1.items():
        print(i)
    return ""

print(convert_tuple())