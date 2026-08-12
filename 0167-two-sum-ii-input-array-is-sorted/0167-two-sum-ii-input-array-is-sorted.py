class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            sum = nums[i]+nums[j]
            if sum == target:
                return [i + 1,j + 1]
            elif sum < target:
                i += 1
            else:
                j -= 1        