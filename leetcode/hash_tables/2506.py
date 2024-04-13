class Solution:
    def similarPairs(self, words: List[str]) -> int:

        vectors_dict = {}
        for word in words:
            vector = [0]*26
            for letter in word:
                vector[97-ord(letter)] = 1
            vector = tuple(vector)
            vectors_dict[vector] = vectors_dict.get(vector, 0) + 1

        ans = 0
        for key, value in vectors_dict.items():
            ans += (value*(value-1)) // 2  # сколько пар чисел
        return ans
