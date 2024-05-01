class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        letters_set = set()
        max_ans = 0

        l = 0
        for r in range(n):
            if s[r] not in letters_set:
                letters_set.add(s[r])
                max_ans = max(max_ans, r - l + 1)
