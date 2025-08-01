class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {']': '[', '}': '{', ')': '('}
        for i in s:
            if i in '[{(':
                stack.append(i)
            else:
                top = stack[len(stack)-1] if len(stack) >= 1 else ''
                result = top == map[i] 
                if result:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0