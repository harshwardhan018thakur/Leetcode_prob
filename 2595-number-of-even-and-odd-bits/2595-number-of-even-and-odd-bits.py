class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        binary = bin(n)[2:]
        even = 0
        odd  = 0
        for i in range(len(binary)):
            if binary[-(i+1)] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even,odd]