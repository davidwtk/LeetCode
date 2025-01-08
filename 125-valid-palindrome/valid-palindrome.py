class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not self.alphanum(s[start]):
                start += 1
            while end > start and not self.alphanum(s[end]):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
            
    
    def alphanum(self, char: str) -> bool:
        return (ord("A") <= ord(char) <= ord("Z") or\
        ord("0") <= ord(char) <= ord("9") or\
        ord("a") <= ord(char) <= ord("z"))