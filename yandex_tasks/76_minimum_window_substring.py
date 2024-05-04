class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters_dict = {}
        for letter in t:
            letters_dict[letter] = letters_dict.get(letter, 0) + 1

        l = 0
        count = len(letters_dict)
        answer_len = len(s) + 1
        answer_str = ''
        for r in range(len(s)):
            if s[r] in letters_dict:
                letters_dict[s[r]] -= 1
                if letters_dict[s[r]] == 0:
                    count -= 1
            while count == 0:
                if r - l + 1 < answer_len:
                    answer_len = r - l + 1
                    answer_str = s[l:r + 1]
                if s[l] in letters_dict:
                    letters_dict[s[l]] += 1
                    if letters_dict[s[l]] > 0:
                        count += 1

                l += 1
        return answer_str
