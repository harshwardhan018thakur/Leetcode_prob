class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxi = float('-inf')
        # n = len(nums)
        # for i in range(n):
        #     pro = 1
        #     for j in range(i,n):
        #         pro *= nums[j]
        #         maxi = max(maxi,pro)
        # return maxi
        current_max = nums[0]
        current_min = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            a = current_max*num
            b = current_min*num
            current_max = max(num,a,b)
            current_min = min(num,a,b) 
            ans = max(ans,current_max)
        return ans