class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in dict:
            if dict[i] > 1:
                return i