class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        deff = {} 
        for i in nums:
            if i in deff:
                deff[i] += 1
            else:
                deff[i] = 1
        for i in deff.values():
            if i >= 2:
                return True
        return False