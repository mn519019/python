# Algorithm to handle postfix expression 
# Evaluate for each character in postfix expression
# If operator is encountered, pop 2 characters from stack which were already filled in stack.
# first = top element of the stack | second = second element from stack
# Check for operator & push into stack after operation
# second operand (operator) first operand
# return top element from stack 

def postfix_expression(list):
    operators = ["+", "-", "*", "/"]
    stack = []
    for i in list:
        # validate whether array items contain operators
        # if it does, add it to the stack
        if i not in operators:
            stack.append(i)
        else:
            first = int(stack.pop())
            second = int(stack.pop())
            if i == "+":
                stack.append(second + first)
            if i == "*":
                stack.append(second * first)
            if i == "-":
                stack.append(second - first)
            if i == "/":
                stack.append(second / first)

    return stack[-1] # return the last element of the stack
        

A = ["2","1","+","3","*"]
print(postfix_expression(A))

# 2 + 1 = 3
# 3 * 3 = 9  