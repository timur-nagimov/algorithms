class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        # сохраняем все произведения чисел из первого списка
        first_dict = {}
        for i in range(n1):
            for j in range(i+1, n1):
                composition = nums1[i]*nums1[j]
                first_dict[composition] = first_dict.get(composition, 0) + 1

        second_dict = {}
        for i in range(n2):
            for j in range(i+1, n2):
                composition = nums2[i]*nums2[j]
                second_dict[composition] = second_dict.get(composition, 0) + 1

        # считаем ответы, суммируем
        ans = 0
        # первый список
        for number in nums1:
            square_number = number*number
            if square_number in second_dict:
                ans += second_dict[square_number]
        # второй список
        for number in nums2:
            square_number = number*number
            if square_number in first_dict:
                ans += first_dict[square_number]

        return ans
