
class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}

        for index, num in enumerate(nums):
            other = target - num

            if other in h:
                return [h[other], index]
            else:
                h[num] = index

        return []

input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))