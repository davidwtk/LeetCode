class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for idx, a in enumerate(nums):

            # Since a will be the smallest entry in the three sum, it must be negative as
            # (b + c) >= a which means (a + b + c) > 0 if a > 0.
            if a > 0:
                break

            # Remove cases of duplicates in the first number
            if idx > 0 and a == nums[idx - 1]:
                continue
            
            start = idx + 1
            end = len(nums) - 1
            while start < end:
                three_sum = a + nums[start] + nums[end]

                if three_sum > 0:
                    end -= 1
                
                elif three_sum < 0:
                    start += 1
                
                else:
                    output.append([a, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    # Ensure that we do not duplicate the two sum combination
                    while nums[start] == nums [start - 1] and start < end:
                        start += 1
        return output