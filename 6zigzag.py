class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or len(s) <=numRows:
            return s
        i=0
        a =[""] * numRows
        st = False
        for index, ch in enumerate(s):
            
            a[i]= a[i]+ch
            if (i == numRows-1) or i == 0 :
                st= not st
            i = i +1 if st else i -1


            
        return "".join(a)
            