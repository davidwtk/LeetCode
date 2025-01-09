class Solution:
    def maxArea(self, height: List[int]) -> int:
        # length = end - start
        # height = min(height[end], height[start])
        # area = length * height

        start, end = 0, len(height) - 1
        max_area = 0
        while start < end:
            area = (end - start) * min(height[end], height[start])
            if area > max_area:
                max_area = area
            if height[end] < height[start]:
                end -= 1
            elif height[start] <= height[end]:
                start += 1
        return max_area