class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x_copy = list(x)
        x_copy.reverse()
        return (x_copy == list(x))

        