#only work for list without any dup

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target =0
        counts = defaultdict(int)
        # counts[0] = 1
        ans = curr = 0

        # nums = sorted(nums)
        for index, num in enumerate(nums):
            counts[num] = index
        # left =0 
        # right=  len(nums)-1
        # while left < right:
        #     value = target - nums[left]+ nums[right]
        #     if target - nums[left]+ nums[right] in counts:
        lists=[]
        for index in range(len(nums)):
            for index2 in range(index+1,len(nums) ):
                value = target - (nums[index]+ nums[index2])
                if value in counts:
                    if index != index2 and index != counts[value]:
                        ans = sorted([nums[index], nums[index2], value])
                        if ans not in lists:
                            lists.append(ans)
        return lists

