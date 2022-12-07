from math import sqrt

class Solution:
    def isPerfectSquare(self, num: int):
        sq_root = int(sqrt(num))
        if num in range(1,pow(2,31)-1) and \
           sq_root*sq_root == num:
            return True
        else:
            return False



if __name__ == "__main__" :
    sol = Solution()
    print(sol.isPerfectSquare(16))
