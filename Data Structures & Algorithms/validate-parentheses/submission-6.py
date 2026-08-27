class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []

        for i in s:
            if i == '(' or i == '[' or i == '{':
                valid_stack.append(i)
            
            if i == ')':
                if len(valid_stack) == 0:
                    return False
                elif valid_stack[-1] == '(':
                    valid_stack.pop()
                else:
                    return False
            
            if i == ']':
                if len(valid_stack) == 0:
                    return False
                elif valid_stack[-1] == '[':
                    valid_stack.pop()
                else:
                    return False

            if i == '}':
                if len(valid_stack) == 0:
                    return False
                elif valid_stack[-1] == '{':
                    valid_stack.pop()
                else:
                    return False
        
        if len(valid_stack) > 0:
            return False
        else:
            return True
                