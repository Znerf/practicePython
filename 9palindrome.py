class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return 0
        
        a = str(x)
        length= len(a)
        for x in range(length//2):
            if a[x] != a[length-1-x]:
                return 0

        return 1
        