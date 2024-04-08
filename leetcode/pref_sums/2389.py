class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pref_sum = [0]*(n+1)
        for i in range(n):
            pref_sum[i+1] = pref_sum[i] + nums[i]

        answer = []
        for query_num in queries:
            added = False
            for i in range(n+1):
                if pref_sum[i] > query_num:
                    answer.append(i-1)
                    added = True
                    break
            if not added:
                answer.append(n)
        return answer
