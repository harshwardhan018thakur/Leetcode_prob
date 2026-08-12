class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n):
        #     count = 0
        #     for j in range(n):
        #         if nums[i] == nums[j]:
        #             count += 1
        #     if count > n//2:
        #         return nums[i]
        # return -1
        n = len(nums)
        mp = {}

        for i in nums:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1

        for key in mp:
            if  mp[key] > n//2:
                return key
        return -1

