class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        sp = {')': '(','}':'{',']':'['}
        for i in s:
            if i in sp:
                if not stack or stack[-1] != sp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0

        