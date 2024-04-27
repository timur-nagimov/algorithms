class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        sorted_freq = sorted(num_dict.items(), key=lambda x: -x[1])

        ans = []
        for i in range(k):
            ans.append(sorted_freq[i][0])
        return ans
