def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):

                if  nums[i]+nums[j] == target:

                    l.append(i)
                    l.append(j)
                    break
                else:
                    pass
        return l

def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            val = target - nums[i]
            if val in dict:
                return [dict[val],i]
            dict.update({nums[i] : i})

def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts={}
        for i, num in enumerate(nums):
            if target - num in dicts.keys():
                return [dicts[target-num], i]
            else:
                dicts[num] = i
