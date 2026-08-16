from typing import List

class Solution:

    def firstoccur(self, nums: List[int], n: int, target: int) -> int:
        low = 0
        high = n - 1
        first = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return first

    def lastoccur(self, nums: List[int], n: int, target: int) -> int:
        low = 0
        high = n - 1
        last = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        first = self.firstoccur(nums, n, target)

        if first == -1:
            return [-1, -1]

        last = self.lastoccur(nums, n, target)

        return [first, last]