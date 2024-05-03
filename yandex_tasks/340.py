class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        letters_dict = {}
        l = 0
        max_ans = 0
        for r in range(len(s)):
            letters_dict[s[r]] = letters_dict.get(s[r], 0) + 1
            if len(letters_dict.keys()) <= k:
                max_ans = max(max_ans, r-l+1)
            else:
                letters_dict[s[l]] -= 1
                if letters_dict[s[l]] == 0:
                    letters_dict.pop(s[l])
                l += 1

        return max_ans
