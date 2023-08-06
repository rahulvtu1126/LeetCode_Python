
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_set=set(nums)
        num_dict_count={}
        for i in nums_set:
            num_dict_count[i]=nums.count(i)
        a=sorted(num_dict_count.items(), key=lambda x: x[1],     reverse=True)
        a=a[:k]
        k_list=[]
        for i in a:
            k_list.append(i[0])
        return k_list
    
    
s=Solution()
nums=[1,1,1,2,2,3]
k = 2
s.topKFrequent(nums,k)

# nums=[1]
# k = 1
# s.topKFrequent(nums,k)

        