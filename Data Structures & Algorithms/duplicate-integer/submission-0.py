class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        numsDict = {}
        for i in range(len(nums)):
            print(numsDict.get(nums[i]), nums[i])
            if numsDict.get(nums[i]) == None:
                numsDict[nums[i]] = 1
            else:
                return True
        
        return False
        