class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window approach
        chars = set()
        left = 0
        highest = 0
        for i in range(len(s)):
            # Remove duplicate from the left until substring is valid
            while s[i] in chars:
                chars.remove(s[left])
                left += 1
            # Add new character into set and check max length of substring
            chars.add(s[i])
            highest = max(highest, i - left + 1)
        return highest