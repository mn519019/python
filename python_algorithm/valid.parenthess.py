# Strategy: Use a stack to pop when the hashmap value is matched with the top of the stack.
# The key is we need to map parentheses in a reverse order to apply this strategy.
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
