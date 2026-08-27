class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        valid_stack = []

        pairs = {')': '(', ']': '[', '}': '{'}

        for pair in s:
            if pair in pairs:
                if valid_stack and valid_stack[-1] == pairs[pair]:
                    valid_stack.pop()
                else:
                    return False
            else:
                valid_stack.append(pair)
        
        if len(valid_stack) > 0:
            return False
        else:
            return True
                