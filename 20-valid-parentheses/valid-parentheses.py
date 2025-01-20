class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
    def isValid(self, s: str) -> bool:
        stack = deque()
        closers = [")", "]", "}"]
        for i in s:
            if i not in closers:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i == ")":
                    if stack.pop() != "(":
                        return False
                elif i == "}":
                    if stack.pop() != "{":
                        return False
                elif i == "]":
                    if stack.pop() != "[":
                        return False
                
        return len(stack) == 0