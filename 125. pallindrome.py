import string
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()
        left = 0 
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left +=1
                continue
            if not s[right].isalnum():
                right -=1
                continue

            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left +=1
                right -=1
            
            
        return True
            



        # while char in str 
        # return s[:len(s)//2] == s[len(s)//2 :]
        