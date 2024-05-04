class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(l for l in s if l.isalnum())
        s = s.lower()

        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
