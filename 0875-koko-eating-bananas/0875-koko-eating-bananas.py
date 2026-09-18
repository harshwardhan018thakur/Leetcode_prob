class Solution:
    def cal_total_hour(self, a: list[int], h: int):
        th = 0
        for i in a:
            th += math.ceil(i/h)
        return th
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        max_piles = max(piles)
        high = max_piles
        ans = max_piles
        while low <= high:
            mid = (low + high)//2
            th = self.cal_total_hour(piles,mid)
            if th <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        