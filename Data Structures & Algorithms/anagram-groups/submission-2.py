class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        an = defaultdict(list)

        for st in strs:
            str_list = [0] * 26
            for i, char in enumerate(st):
                str_list[ord(char)-ord('a')] +=1

            an[tuple(str_list)].append(st)

        return list(an.values())
