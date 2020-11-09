#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
@Author  : Dan Yang
@Date    : 2020/10/30 17:09

'''


#!/usr/bin/python3
# -*-coding:utf-8 -*-

'''
二叉树的前序遍历（字节跳动、谷歌、腾讯在半年内面试中考过）
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
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

    def preorder(self, root):
        # 前序遍历，递归做法
        # 时间复杂度：o(n)--所有节点只遍历一遍
        # 空间复杂度：O(n)---树的深度

        if not root:
            return  []

        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def preorder_stack(self, root):
        # 前序遍历，堆栈做法，先放入根，再依次压入左，右
        # 时间复杂度：遍历1遍，O(N)
        # 空间复杂度：o(n)
        if not root:
            return []

        ret, cur, stack = [], root, []
        while cur or stack:
            while cur:
                ret.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right

        return ret


if __name__ == '__main__':

    sl = Solution()
    cases = [[1, 'null', 2, 3]]

    for case in cases:
        print('input:\n', case)
        root = create_bt_list(case, 0)

        result = sl.preorder_stack(root)

        print('result:', result)



