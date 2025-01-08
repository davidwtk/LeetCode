class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        pre[0] = 1
        post[-1] = 1
        start, end = 1, 1
        # Return product of elements before each index
        for i in range(1, len(nums)):
            start *= nums[i - 1]
            pre[i] = start

        # Product of elements after each index
        for i in range(len(nums) - 2, -1, -1):
            end *= nums[i + 1]
            post[i] = end
        
        # Combine both before and after
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = pre[i] * post[i]
        return output