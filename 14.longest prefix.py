class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        longest = strs[0]

        for string in strs[1:]:
            if longest=='':
                return ""
            minimumCount = min(len(string),len(longest))
            if len(longest) > len(string):
                longest=longest[0:len(string)]
            for i in range(minimumCount):
                print(string[i],longest[i])
                if string[i]!= longest[i]:
                    longest= longest[0:i]
                    break
                
        return longest
        