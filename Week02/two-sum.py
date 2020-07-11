class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in pair:
                return [pair[tmp],i]
            else:
                pair[nums[i]] = i
