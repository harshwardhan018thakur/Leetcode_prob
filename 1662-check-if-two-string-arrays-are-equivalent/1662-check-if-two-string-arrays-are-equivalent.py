class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        wordi1 = "".join(word1)
        wordi2 = "".join(word2)
        if len(wordi1) != len(wordi2):
            return False
        i, j = 0, 0
        while i < len(wordi1) and j < len(wordi2):
            if wordi1[i] != wordi2[j]:
                return False
            i += 1
            j += 1
        return True
        