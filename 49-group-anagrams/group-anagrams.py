class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for i in strs:
            letters = [0] * 26

            for j in i:
                letters[ord(j) - 97] += 1
            letters = tuple(letters)
            if letters in word_dict:
                word_dict[letters].append(i)
            else:
                word_dict[letters] = [i]
                
        
        return list(word_dict.values())