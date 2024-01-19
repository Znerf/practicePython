class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort =[]
        county = 0
        countx = 0
        
        n= len(nums1)
        m= len(nums2)
        while countx< n  or  county< m :

            x= nums1[countx] if countx< n else None
            y = nums2[county] if county< m else None

            if x is not None and ( y is None or y > x):
                sort.append(x)
                countx +=1
            else :
                sort.append(y)
                county +=1
        if len(sort)%2 ==0 :
            return (sort[len(sort) // 2 -1] +sort[len(sort) // 2 ])/2
        else:
            return (sort[len(sort) // 2])
        return sort