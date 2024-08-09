class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs= sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return first[0:i] 
        return first
        