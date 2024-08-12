class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = []
        nums.sort()
        flag=True
        close = sum(nums[0:3])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(close-target) :
                    close =  total
                if total == target :
                    return total

                if total > target:
                    k -= 1
                # elif total < 0:
                #     j += 1
                else:
                    # res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                
        
        return close