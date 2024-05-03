class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        ans = 0
        i = 0
        while i < n:
            let_count = 0
            letter = chars[i]
            while i < n and letter == chars[i]:
                let_count += 1
                i += 1
            # плюсуем сам символ
            # также ans является указателем куда ставить
            chars[ans] = letter
            ans += 1
            if let_count > 1:
                # плюсуем разряд числа
                for place_number in str(let_count):
                    chars[ans] = place_number
                    ans += 1

        return ans
