class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 0

        sDic={}
        tDic={}

        for st in s:
            sDic[st] = sDic[st]+1 if st in sDic else 1
        
        for st in t:
            tDic[st] = tDic[st]+1 if st in tDic else 1
            if st not in sDic or tDic[st]>sDic[st]:
                return 0
        return 1