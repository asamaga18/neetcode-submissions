class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if x == ')':
                    if check != '(':
                        return False
                elif x == '}':
                    if check != '{':
                        return False
                else:
                    if check != '[':
                        return False
        if stack:
            return False
        return True