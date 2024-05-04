class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in ans_dict:
                ans_dict[sorted_word].append(word)
            else:
                ans_dict[sorted_word] = [word]

        ans = []
        for values in ans_dict.values():
            ans.append(values)
        return ans
