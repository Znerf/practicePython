class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        def backtrack(nums,start,total):
            if len(start) == 4:
                if target == total:
                    if start not in solu:
                        solu.append(start.copy())
                return

            if len(nums) < 4-(len(start)):
                return

            for i,val in enumerate(nums):
                start.append(val)
                total=total+val
                backtrack(nums[i+1:],start,total)
                start.pop()
                total=total-val
            
        solu=[]
        backtrack(nums,[],0)
        return solu

