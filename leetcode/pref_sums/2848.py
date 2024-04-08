class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        n = len(nums)
        edges_numbers = [0]*(102)
        for x1, x2 in nums:
            edges_numbers[x1] += 1
            edges_numbers[x2+1] -= 1
        pref_sums = [0]*(102)
        for i in range(101):
            pref_sums[i+1] = pref_sums[i] + edges_numbers[i]

        counter = 0
        for i in pref_sums:
            if i != 0:
                counter += 1
        return counter
