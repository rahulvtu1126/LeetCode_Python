class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set=set(nums)
        #print(len(nums),len(nums_set) )
        if len(nums) != len(nums_set):
            return 'true'
        elif len(nums) == len(nums_set):
            return 'false'

s=Solution()
# nums=[1,2,3,1]
# s.containsDuplicate(nums)
# nums=[1,2,3,4]
# s.containsDuplicate(nums)
# nums=[1,1,1,3,3,4,3,2,4,2]
# s.containsDuplicate(nums)