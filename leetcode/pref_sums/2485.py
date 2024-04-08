class Solution:
    def pivotInteger(self, n: int) -> int:
        pref_sum = []
        number = 0
        for i in range(n):
            pref_sum.append(number+i+1)
            number += i+1

        suf_sum = []
        number = 0
        for i in range(n-1, -1, -1):
            suf_sum.append(number+i+1)
            number += i+1
        suf_sum.reverse()

        for i in range(n):
            if pref_sum[i] == suf_sum[i]:
                return i+1
        return -1
