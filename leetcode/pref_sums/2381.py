class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pref_sum = [0]*(n+1)
        for start, end, direction in shifts:
            pref_sum[start] += 1 if direction else -1
            pref_sum[end+1] += -1 if direction else 1
        # Поиск самой суммы
        for i in range(n):
            pref_sum[i+1] += pref_sum[i]
        print(pref_sum)

        ans = ''
        for i in range(n):
            letter_num = ord(s[i]) + pref_sum[i] % 26
            # 122 - код буквы z
            # 97 - код буквы 'a'
            # -123 для переноса в начало алфавита
            if letter_num > 122:
                letter_num = 97 + letter_num - 123
            ans = f'{ans}{chr(letter_num)}'
        return ans
