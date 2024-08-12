class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0

        nums =sorted(nums)
        res =[]
        for index, num in enumerate(nums):
            left = index+1
            right = len(nums)-1

            while left < right:
                val = num + nums[left] + nums[right]
                if val == target: 
                    value =  [num, nums[left], nums[right]]
                    left = left + 1
                    if value not in res:
                        res.append(value)

                print(val, target)
                if val > target:
                    right = right - 1
                if val < target:
                    left = left + 1
        return res


