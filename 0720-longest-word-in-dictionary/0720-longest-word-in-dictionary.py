class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        st = set()
        ans = ""
        for i in words:
            if len(i) == 1 or i[:-1] in st:
                st.add(i)
                if len(i) > len(ans):
                    ans = i
        return ans