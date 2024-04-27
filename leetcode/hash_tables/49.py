class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            tmp_list = words_dict.get(sorted_word, [])
            tmp_list.append(word)
            words_dict[sorted_word] = tmp_list

        ans = []
        for key, val in words_dict.items():
            ans.append(val)

        return ans
