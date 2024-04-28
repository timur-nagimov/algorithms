class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        mask_dict = {')': '(', ']': '[', '}': '{'}

        for l in s:
            if l in mask_dict.values():
                open_stack.append(l)
            elif not open_stack or mask_dict[l] != open_stack.pop():
                return False

        return not open_stack
