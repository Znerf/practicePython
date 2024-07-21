class Solution:
    def reverse(self, x: int) -> int:  
        pos= 1
        if x < 0:
            pos = -1
            x = x*-1
        s=0
        while x !=0:
            rem = x % 10
            x= x // 10
            s= s*10 +rem
        return s*pos if -2**31 <= s*pos <= 2**31 - 1 else 0



        