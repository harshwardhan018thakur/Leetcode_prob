class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            count = 0
            conti = chars[read]
            while read < len(chars) and chars[read] == conti:
                read += 1
                count += 1
            chars[write] = conti
            write += 1
            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1
        return write

        
        