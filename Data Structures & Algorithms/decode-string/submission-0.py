class Solution:
    def decodeString(self, s: str) -> str:
        current_str = ""
        current_num = 0
        stack = []

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == "[":
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0

            elif char.isalpha():
                current_str += char

            elif char == ']':
                prev_str, repeat = stack.pop()
                current_str = prev_str + current_str * repeat

        return current_str
            