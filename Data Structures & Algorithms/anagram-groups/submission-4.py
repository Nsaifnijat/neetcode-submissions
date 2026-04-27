class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        an = defaultdict(list)

        for st in strs:
            key = [0]*26
            for s in st:
                key[ord(s) - ord('a')] += 1
            
            an[tuple(key)].append(st)
        return list(an.values())