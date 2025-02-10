class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        #creating a map to store array elements along with their index
        hashmap = {}  
        for i in range(len(nums)):
            hashmap[nums[i]] = i


        for i in range(len(nums)):
            complement = target - nums[i]
            # checking whether the complement is present in the map and its index is not equal to the current index
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

        return [] #if no valid pair is found