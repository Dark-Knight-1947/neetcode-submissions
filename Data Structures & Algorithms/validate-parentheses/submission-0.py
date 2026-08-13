class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictt = {")" : "(", "]" : "[", "}" : "{"}
        for ch in s:
            if ch in dictt:
                if stack and stack[-1] == dictt[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False