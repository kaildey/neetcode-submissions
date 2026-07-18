class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        openers = "({["
        closers = ")}]"

        for i in range(len(s)):
            if s[i] in openers:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == openers[closers.index(s[i])]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False