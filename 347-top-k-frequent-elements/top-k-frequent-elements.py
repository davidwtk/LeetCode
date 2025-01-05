class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele_dict = {}
        for i in nums:
            if i in ele_dict:
                ele_dict[i] += 1
            else:
                ele_dict[i] = 1
        ele_count = [[k, v] for k, v in sorted(ele_dict.items(), key = lambda x: x[1], reverse=True)]
        output = []
        for j in range(k):
            output.append(ele_count[j][0])
        return output