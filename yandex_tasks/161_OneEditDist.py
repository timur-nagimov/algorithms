# 1. just false: abcde - abc
# 2. edit one: abed - abcd
# 3. remove one: abec - abc
# 4. add one: abcd - abced

# i - индекс несовпавших элементов
# 1. Если длина различается более чем на 1 - False
# 2. Надо проверить, что s[i+1:] = t[i+1:]
# 3. Надо проверить, что s[i+1:] = t[i:]
# 4. Надо проверить, что s[i+1:] = t[i:]


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                if s[i+1:] != t[i+1:] and s[i+1:] != t[i:] and s[i:] != t[i+1:]:
                    return False
                break
        return True
