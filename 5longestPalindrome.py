# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
   
    def longestPalindrome(self, s: str) -> str:
        longest=''
        maxLen=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                word=s[i:j+1]
                if word == word[::-1] and len(word)>maxLen:
                    longest = word
                    maxLen= len(longest)
        
        return longest