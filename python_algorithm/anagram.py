# We are given two strings like "cinema" and "iceman" as inputs. Can you write a method isAnagram(str1, str2) 
# that will return true or false depending on whether the strings are anagrams of each other?
def is_anagram(str1, str2):
    ## fill this in
    l1 = list(str1.lower())
    l2 = list(str2.lower())
    if len(l1) == len(l2):
        l1.sort()
        l2.sort()
    return l1 == l2


print("Result: ",is_anagram('cinema', 'iceman'))

# import unittest

# class Test(unittest.TestCase):
#     def test_1(self):
#         assert is_anagram("Mary", "Army") == True
#         print("PASSED: is_anagram('Mary', 'Army') should return False")

#     def test_2(self):
#         assert is_anagram("cinema", "iceman") == True
#         print("PASSED: is_anagram('cinema', 'iceman') should return True")

#     def test_3(self):
#         assert is_anagram("jake", "jay") == False
#         print("PASSED: is_anagram('jake', 'jay') should return False")

# if __name__ == "__main__":
#     unittest.main(verbosity=2)
#     print("Nice job, 3/3 tests passed!")
