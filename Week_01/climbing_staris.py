#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/9/30 14:48

'''

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

链接：https://leetcode-cn.com/problems/climbing-stairs
'''

class Solution(object):
    # 寻找重复性
    # step1 每次可爬1或2个台阶，即到n的时候，可以在n-1采用爬1阶到达，或者在n-2的时候，采用2阶到达
    # 以n-1为目标的时候，重复step1 的操作，即重复性
    # f(n) = f(n-1) + f(n-2)

    # 方法1：递归计算，树深度为n, 时间复杂度为O(2^n)，且节点有重复---pass
    # 方法2：将计算的中间值放入缓存，时间复杂度为O(n)， 空间复杂为O(1)
    # 方法3：因只需计算n的对应值，采用3个变量代替，不断替换

    def climb_stairs_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        sums = [0] * n
        sums[0:3] = [1, 2, 3]
        for i in range(2, n):
            sums[i] = sums[i-1] + sums[i-2]
        return sums[-1]

    def climb_stairs_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        sums = [1, 2, 3]
        for i in range(2, n-1):
            sums.append(sums[i] + sums[i-1])

        return sums[-1]


    def climb_stairs_3(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        fa, fb, fc = 1, 2, 3

        for i in range(3, n+1):
            fc = fa + fb
            fa = fb
            fb = fc

        return fc



if __name__ == '__main__':

    sl = Solution()

    test_cases = [3, 4, 5, 0, 1, 2]

    for case in test_cases:
        print('\ninput:', case)
        result = sl.climb_stairs_2(case)
        print('output:', result)
