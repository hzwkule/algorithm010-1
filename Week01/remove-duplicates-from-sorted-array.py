class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        tmp = nums[0]
        counter = 0
        for i in range(1,len(nums)):
            if nums[i] != tmp:
                tmp = nums[i]
                counter += 1
                nums[counter] = tmp
        return counter + 1
