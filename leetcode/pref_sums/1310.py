class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pref_xor = [0]*(n+1)
        for i in range(n):
            pref_xor[i+1] = pref_xor[i] ^ arr[i]

        answer = []
        for left, right in queries:
            answer.append(pref_xor[right+1] ^ pref_xor[left])
        return answer
