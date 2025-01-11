class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, no substring exists
        if len(s1) > len(s2):
            return False

        # Make array to store counts of each letter in s1 and window of s2
        chars1, chars2 = [0] * 26, [0] * 26

        # Make initial window for s2 of same size as s1 and compare with s1
        for i in range(len(s1)):
            chars1[ord(s1[i]) - 97] += 1
            chars2[ord(s2[i]) - 97] += 1
        
        # Check if permutation exists in initial window.
        if chars1 == chars2:
            return True

        # Repeat by sliding window across s2
        left = 0
        for i in range(len(s1), len(s2)):
            chars2[ord(s2[i]) - 97] += 1
            chars2[ord(s2[left]) - 97] -= 1
            if chars1 == chars2:
                return True
            left += 1
        return False