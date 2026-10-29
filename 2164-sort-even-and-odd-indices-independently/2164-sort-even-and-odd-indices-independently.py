class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        # sorting both odd and even list
        odd.sort(reverse=True)
        even.sort()
        i = 0
        k = 0
        for j in range(len(nums)):
            if j % 2 == 0:
                nums[j] = even[i]
                i += 1
            else:
                nums[j] = odd[k]
                k += 1
        return nums