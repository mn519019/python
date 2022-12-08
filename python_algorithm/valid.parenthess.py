class Solution:
    def isValid(self,s:str):
        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}

        for x in s:
            if x in closeToOpen:
                if stack and stack[-1] == closeToOpen[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False

# Driver Code
if __name__ == "__main__" :               
    sol = Solution()
    print(sol.isValid("{}"))     # Expect True
    print(sol.isValid("[{}]"))   # Expect True
    print(sol.isValid("[{]}"))   # Expect False
