
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b) 
    }

        for token in tokens:
            if token in ops:
                operation = ops[token]
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operation(num1,num2))
            else:
                stack.append(int(token))

        return stack.pop()