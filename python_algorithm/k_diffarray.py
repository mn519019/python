from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        c = Counter(nums)
        count = 0
        print("the hashmap of array",c.items())
        
        if k == 0:
            for key,v in c.items():
                if v > 1:
                    count+=1
        else:
            for key,v in c.items():
                if key+k in c:
                    count+=1
        return count

arr = [3,1,4,1,5]
k = 0
s = Solution()
print ("Count of pairs with given diff is ",
                s.findPairs(arr,k))
