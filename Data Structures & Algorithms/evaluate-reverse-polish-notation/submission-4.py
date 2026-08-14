class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op == '+':   
                stack.append(stack.pop() + stack.pop())
            elif op == '-':
                stack.append(- (stack.pop() - stack.pop()))
            elif op == '*':
                stack.append(stack.pop() * stack.pop())
            elif op == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(op))
        return stack[-1]