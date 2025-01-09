class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since O(1) space, cannot use hashmap. Time Complexity: O(n)
        # Approach with pointers. But how? Since array is sorted in ascending order
        start = 0
        end = len(numbers) - 1
        num_sum = numbers[start] + numbers[end]
        while (num_sum) != target:
            num_sum = numbers[start] + numbers[end]
            if (numbers[end] > target) and (num_sum > target):
                end -= 1
                
            elif (num_sum) > target:
                end -= 1
            
            elif (num_sum) < target:
                start += 1
        return [start + 1, end + 1]