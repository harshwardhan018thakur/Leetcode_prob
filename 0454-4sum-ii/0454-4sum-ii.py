class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        # tc of below code is o(n^4)
        # ans = 0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         for k in range(len(nums3)):
        #             for l in range(len(nums4)):
        #                 sum = nums1[i] + nums2[j] + nums3[k] + nums4[l]
        #                 if sum == 0:
        #                     ans += 1
        # return ans
        freq_sum = {}
        ans = 0
        # calclulating the sum of first two list with all possibilty and stroing in freq dict
        for i in nums1:
            for j in nums2:
                sumi = i+j
                freq_sum[sumi] = freq_sum.get(sumi,0)+1
        # a +b = -(c+d) and checking wether apposite is there in dict or not
        for i in nums3:
            for j in nums4:
                required = -(i+j)
                ans += freq_sum.get(required,0)
        return ans

        