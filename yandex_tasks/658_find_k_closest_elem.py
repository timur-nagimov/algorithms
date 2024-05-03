class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = n - k

        while l < r:
            mid = (l + r) // 2
            if (x - arr[mid]) <= (arr[mid+k]-x):
                r = mid
            else:
                l = mid + 1

        return arr[l:l+k]
