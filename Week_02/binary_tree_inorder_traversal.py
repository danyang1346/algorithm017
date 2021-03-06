#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/10/11 21:40

'''
'''
二叉树的中序遍历（亚马逊、字节跳动、微软在半年内面试中考过）
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
'''

class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 将输入的列表转为一个二叉树，返回根节点
def create_bt_list(lst, start):
    if start < len(lst):
        if lst[start] == 'null':
            return None
        else:
            root = TreeNode(lst[start])
            root.left = create_bt_list(lst,  start + 1)
            root.right = create_bt_list(lst, start + 2)
            return root

    return None

class Solution(object):

    def inorder1(self, root):
        '''

        :param root:
        :return:
        '''
        # 方法1：递归算法
        # 时间复杂度：O(n)
        # 空间复杂度：O(h) 树的深度
        if not root:
            return []

        return self.inorder1(root.left) + [root.val] + self.inorder1(root.right)

    def inorder2(self, root):

        # 方法2：堆栈实现
        # 堆，先进后出，中序遍历，先左(到底)再中后右
        # 时间复杂度O(n)
        # 空间复杂度O(n)--栈的深度
        if not root:
            return []

        stack = []
        cur = root
        ret = []
        while cur or len(stack) > 0:
            while  cur :
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ret.append(cur.val)
            cur = cur.right

        return ret


if __name__ == '__main__':

    sl = Solution()
    cases = [[1, 'null', 2, 3]]

    for case in cases:
        print('input:\n', case)
        root = create_bt_list(case, 0)

        result = sl.inorder2(root)

        print('result:', result)



