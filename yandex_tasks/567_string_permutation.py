class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        dict2 = {}
        for symbol in s1:
            dict1[symbol] = dict1.get(symbol, 0) + 1

        l = 0
        cur_length = 0
        for r in range(len(s2)):
            if cur_length < len(s1):
                dict2[s2[r]] = dict2.get(s2[r], 0) + 1
                cur_length += 1
            if cur_length == len(s1):
                if dict1 == dict2:
                    return True
                dict2[s2[l]] -= 1
                if dict2[s2[l]] == 0:
                    dict2.pop(s2[l])
                l += 1
                cur_length -= 1

        return False
