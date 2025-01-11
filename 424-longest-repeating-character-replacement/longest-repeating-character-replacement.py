class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # output
        res = 0
        # charSet only contains distinct characters
        charSet = set(s)

        # For each distinct character, O(26n) where n is the length of s -> linear time
        for c in charSet:
            count = l = 0
            # Count how many times each character appears
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                # Length of substring - count shows the amount of replacement letters used so far
                # If it is more than k, then we have exceeded the limit. This means we need to shift
                # the sliding window on the left side to the right until we get back in the limit.
                while (r - l + 1) - count > k:
                    # If we slide over the char, c, we are counting, need to decrement counter
                    # Else, no change to number of char c.
                    if s[l] == c:
                        count -= 1
                    l += 1
                    
                res = max(res, r - l + 1)
        return res