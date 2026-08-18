class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        # count freq of each element 
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        sort_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ans = ""
        for ch,count in sort_freq:
            ans += ch*count
        return ans
        