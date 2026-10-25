class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sum = {}
        l=[]
        for i in range(0, len(nums)):
            dif = target - nums[i]
            # print(l)
            if dif in hash_sum.keys():
                # print(i, hash_sum[dif])
                l.append(hash_sum[dif])
                l.append(i)
                # print(l)
            else:
                hash_sum[nums[i]] = hash_sum.get(nums[i], i)
        return l