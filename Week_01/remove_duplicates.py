#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/9/27 16:06

'''

'''
26. 删除排序数组中的重复项

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def remove_duplicates(self, nums):
        '''
        :param nums: list[int]
        :return: int
        '''
        # 思路：双指针法，快慢指针，慢的标记非重复的位置，快的遍历整个数组
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)

        if not nums:
            return 0

        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                # 因为j其实索引从0开始，第一个位置不会出现重复，所以前置加1，再赋值
                if i - j > 1:
                    j += 1
                    nums[j] = nums[i]

        return j + 1

        # count = 0
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         count += 1
        #     else:
        #         nums[i-count] = nums[i]
        # return len(nums) - count


if __name__ == '__main__':

    sl = Solution()

    test_cases = [[], [1], [1,1,2], [0,0,1,1,1,2,2,3,3,4]]

    for case in test_cases:
        print('\ninput:', case)
        result = sl.remove_duplicates(case)
        print('output:', result, case[:result])



