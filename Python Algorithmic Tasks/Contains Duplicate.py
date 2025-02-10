from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        # using a set to store elements pf list  uniquely
        # iterate over the elements of list and if the number is already been seen in set then return true otherwise add it to the set 
        for num in nums:
            if num in hashmap:
                return True
            hashmap.add(num)
        return False