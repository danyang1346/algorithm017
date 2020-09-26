#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/9/27 00:20

'''

'''
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):

    def move_zeros_1(self, nums):
        '''
        :param nums: list[int]
        :return: None Do not return anything, modify nums in-place instead
        '''
        # 方法1：找到0元素，并计数，将非零元素依次赋值到前部分，后半部分肯定为0，直接将其赋值为0
        # 时间复杂度为O(n)
        # 空间复杂度为O(1)
        if not nums:
            return []

        count_zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count_zeros] = nums[i]
                count_zeros += 1

        nums[count_zeros:] = [0]*(len(nums)-count_zeros)


    def move_zeros_2(self, nums):
        '''
        :param nums: list[int]
        :return: None , Do not return anything, modify nums in-place instead
        '''
        # 思路：快慢指针，慢指针记录0元素的位置， 快指针遍历整个数值，
        #       当快指针对应元素非0时，快慢指针值交换，两指针同时移动，否则，仅快指针移动
        # 时间复杂度：O(n) 遍历一次数组
        # 空间复杂度: O(1) 无外用空间

        if not nums:
            return []

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1



if __name__ == '__main__':

    sl = Solution()

    test_cases = [[0], [0, 1], [0, 1, 0, 3, 2], [0, 0, 0, 0, 3]]

    for case in test_cases:
        print('\ninput:', case)
        # sl.move_zeros_1(case)
        sl.move_zeros_2(case)
        print('output:', case)
