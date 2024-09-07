class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return (max(max(nums)*nums[0]*nums[1],max(nums)*nums[-2]*nums[-3]))