class Solution:
    def countSegments(self, s: str) -> int:
        a = s.split(" ")
        count = 0
        for i in a:
            if i != "":
                count += 1
        return count
        