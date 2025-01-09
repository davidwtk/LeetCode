class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        total = 0
        leftmax = height[start]
        rightmax = height[end]
        while start < end:
            if leftmax < rightmax:
                start += 1
                leftmax = max(leftmax, height[start])
                total += (leftmax - height[start])
            else:
                end -= 1
                rightmax = max(rightmax, height[end])
                total += (rightmax - height[end])
        return total