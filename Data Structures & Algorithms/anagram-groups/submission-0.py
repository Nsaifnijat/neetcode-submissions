class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups={}
        
        for st in strs:

            count = [0]*26
            for s in st:
                count[ord(s)- ord('a')] +=1
            
            count = tuple(count)
            if count not in groups:
                groups[count]=[]
            groups[count].append(st)
        print(groups)
        return list(groups.values())
