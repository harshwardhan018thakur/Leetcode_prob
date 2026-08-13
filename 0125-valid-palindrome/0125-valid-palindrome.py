class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for x in s:
            if x.isalnum():
                temp += x.lower()
        return temp == temp[::-1]