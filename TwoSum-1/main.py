# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#https://leetcode.com/problems/two-sum/

# %%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        self.rtarget = []
        for x in range(len(self.nums)):
            for y in range(len(self.nums)):
                if x != y and  (self.nums[x] +self.nums[y]) == self.target :
                    self.rtarget.append(x)
                    self.rtarget.append(y)
                    return self.rtarget

