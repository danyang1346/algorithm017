#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/9/28 10:38

'''

# /Users/yangdan/Desktop/区域实时接单率/code/predict.py
# /Users/yangdan/Desktop/区域接单率预测v3/code/predict.py

'''
vimdiff /Users/yangdan/Desktop/区域实时接单率/code/feature_select.py /Users/yangdan/Desktop/区域接单率预测v3/code/feature_select.py
'''
class Solution(object):
    def quick_sort(self, nums, left, right):

        if left >= right:
            return

        low, high = left, right
        base = nums[low]

        while low < high:
            while low < high and nums[high] >= base:
                high -= 1
            nums[low] = nums[high]

            while low < high and nums[low] <= base:
                low += 1
            nums[high] = nums[low]

        nums[low] = base

        self.quick_sort(nums, left, low-1)
        self.quick_sort(nums, low+1, right)




if __name__ == '__main__':

    sl = Solution()
    nums = [3, 2, 8, 5, 1]

    print('orig',  nums)
    # sl.insert_sort(nums)
    # sl.insert_shell(nums)
    # sl.shell_sort(nums)
    # sl.select_sort(nums)
    # result = sl.merge_sort(nums)
    # print(result)
    # sl.bubble_sort(nums)
    # result = sl.insertionSort(nums)
    # print(result)
    # sl.quickSort1(nums, 0, len(nums)-1)

    # result = sl.findValue(nums, 0, len(nums)-1, 2)
    # print(result)

    sl.quick_sort(nums, 0, len(nums) - 1)
    print(nums)

    pass