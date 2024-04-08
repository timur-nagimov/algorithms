class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        for i in range(1, n+1, 2):
            for j in range(n-i+1):
                answer += sum(arr[j:i+j])
        return answer
