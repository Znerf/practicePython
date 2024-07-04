class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        location ={}
        value=[-1,-1]
        for index, character in enumerate(s):
            if (character in location):
                if index-location[character] > value[1]-value[0]:
                    value=[location[character],index]
                location[character]=index
            location[character] = index

            if index == len(s)-1:
                if len(s)-min(location.values) > value[1]-value[0]:
                    value=[min(location.values,len(s))]
        if (value == [-1,-1]):
            return len(s)
        return value[1]-value[0]
if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("aab") == 2