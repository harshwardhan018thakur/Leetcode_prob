class Solution:
    def minSubArrayLen(self, x: int, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        curr_sum = 0
        res = float('inf')
        for  j in range(n):
            curr_sum += arr[j]
            while curr_sum >= x:
                res = min(res,j-i+1)
                curr_sum -= arr[i]
                i += 1
        return 0 if res == float('inf') else res
