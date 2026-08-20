class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        n = len(arr)
        
        arr.sort()
        res = []
        
        # Checking for all possible overlaps
        for i in range(n):
            start = arr[i][0]
            end = arr[i][1]
        
            # Skipping already merged intervals
            if res and res[-1][1] >= end:
                continue
        
            # Find the end of the merged range
            for j in range(i + 1, n):
                if arr[j][0] <= end:
                    end = max(end, arr[j][1])
            res.append([start, end])
        
        return res