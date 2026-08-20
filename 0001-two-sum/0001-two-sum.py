class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] == target:
        #             return[i,j]
        
        # -------second approach -------
        # n = len(nums)
        seen = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp],i]
            seen[num] = i