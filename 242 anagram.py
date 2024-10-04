class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return 0

        # sDic={}
        # tDic={}

        # for st in s:
        #     sDic[st] = sDic[st]+1 if st in sDic else 1
        
        # for st in t:
        #     tDic[st] = tDic[st]+1 if st in tDic else 1
        #     if st not in sDic or tDic[st]>sDic[st]:
        #         return 0
        # return 1

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s == sorted_t

        if len(s) != len(t):
            return 0

        sDic={}
        tDic={}

        for x in range(len(s)):
            sDic[s[x]] =  1 + sDic.get(s[x],0)#sDic[s[x]]+1 if s[x] in sDic else 1
            tDic[t[x]] = 1+ tDic.get(t[x],0) #tDic[t[x]]+1 if t[x] in tDic else 1
            
        return sDic == tDic