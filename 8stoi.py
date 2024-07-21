class Solution:
    def myAtoi(self, s: str) -> int:
        pos=1
        flag=True
        num=0
        for x in s:
            if x == " " and flag:
                continue
            if x == "-" and flag :
                pos= -1
                flag = False
                continue
            if x == "+" and flag:
                flag = False
                continue
            
            if (48 > ord(x) or ord(x) > 75):
                if num*pos < -2 ** 31:
                    return   -2 ** 31
                if num*pos >  2**31 - 1 :
                    return  2**31 - 1
                return num*pos
            num = num*10+ord(x)-48
            flag = False
            
        if num*pos < -2 ** 31:
            return   -2 ** 31
        if num*pos >  2**31 - 1 :
            return  2**31 - 1
        return num*pos
                


                    
        