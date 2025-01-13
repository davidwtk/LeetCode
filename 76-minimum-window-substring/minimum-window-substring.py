class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        charset = set(t)
        s_tally, t_tally = [0] * 58, [0] * 58

        # Populate t_tally to count frequencies of characters in t
        for char in t:
            t_tally[ord(char) - ord("A")] += 1

        left, right = 0, 0
        formed = 0  # Tracks how many characters in t are fully matched
        required = len([char for char in t_tally if char > 0])  # Number of unique chars in t

        shortest = float("inf")
        start_idx = 0

        while right < len(s):
            # Add character at `right` to the window
            char = s[right]
            idx = ord(char) - ord("A")
            s_tally[idx] += 1

            # Check if this character contributes to forming a valid window
            if char in charset and s_tally[idx] == t_tally[idx]:
                formed += 1

            # Try to shrink the window from the left
            while left <= right and formed == required:
                # Update the shortest window
                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    start_idx = left

                # Remove the character at `left` from the window
                left_char = s[left]
                left_idx = ord(left_char) - ord("A")
                s_tally[left_idx] -= 1

                # Check if this breaks the window validity
                if left_char in charset and s_tally[left_idx] < t_tally[left_idx]:
                    formed -= 1

                left += 1

            # Expand the window by moving `right`
            right += 1

        return "" if shortest == float("inf") else s[start_idx:start_idx + shortest]
        