# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # postorder
        if not root:
            return 0

        cameraNeed, cover, count = self.dfs(root, False)
        return max(1, count)

    def dfs(self, root, has_parent):
        if not root:
            return False, True, 0
        if not root.left and not root.right:
            return False, False, 0

        cameraNeedL, coverL, cntL = self.dfs(root.left, True)
        cameraNeedR, coverR, cntR = self.dfs(root.right, True)

        cameraNeed, cover, cnt = False, False, 0

        if cameraNeedL or cameraNeedR:
            cover = True

        if not coverL or not coverR:
            cameraNeed = True
            cover = True
            cnt = 1

        if not cameraNeedL and not cameraNeedR and not has_parent:
            cnt = 1

        return cameraNeed, cover, cntL + cntR + cnt


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # 3 cases for each nodes --> 1) not camera but cover by P 2) not camera but covered by child 3) has camera
        memo = {}
        return min(self.dfs(root, False, False, memo), self.dfs(root, False, True, memo))

    def dfs(self, root, covered, camera, memo):
        if (root, covered, camera) in memo:
            return memo[root, covered, camera]

        if not root:
            if not camera:
                return 0
            else:
                return float('inf')

        # case1: if root has camera, cover children --> child: covered, install or not install
        if camera:
            res = 1 \
                  + min(self.dfs(root.left, True, False, memo), self.dfs(root.left, True, True, memo)) \
                  + min(self.dfs(root.right, True, False, memo), self.dfs(root.right, True, True, memo))


        else:
            if covered:  # case2: if root has no camera, but covered --> child: not be covered, install or not install
                res = 0 \
                      + min(self.dfs(root.left, False, False, memo), self.dfs(root.left, False, True, memo)) \
                      + min(self.dfs(root.right, False, False, memo), self.dfs(root.right, False, True, memo))
            else:  # case3: if root has no camera and not covered --> child: not be covered, one of camera must be installed to cover root
                res = min(self.dfs(root.left, False, False, memo) + self.dfs(root.right, False, True, memo),
                          self.dfs(root.left, False, True, memo) + self.dfs(root.right, False, False, memo),
                          self.dfs(root.left, False, True, memo) + self.dfs(root.right, False, True, memo))

        memo[root, covered, camera] = res
        return memo[root, covered, camera]


class Solution5:  # 贪心思想
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        self.no_c_but_covered = 1
        self.has_camera = 2
        self.no_cover = 3

        if not root:
            return 0
        if self.dfs(root) == self.no_cover:
            self.res += 1
        return self.res

    def dfs(self, root):
        if not root:
            return self.no_c_but_covered

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left == self.no_cover or right == self.no_cover:
            self.res += 1
            return self.has_camera

            # 如果左右子节点有一个有相机，那么当前节点就不需要相机了，否则返回一个没有相机的标记
        if left == self.has_camera or right == self.has_camera:
            return self.no_c_but_covered
        else:
            return self.no_cover


class Solution6:  # 贪心思想
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # no_c_but_covered = 0
        # self.has_camera = 1
        # self.no_cover = -1

        if not root:
            return 0
        if self.dfs(root) == -1:
            self.res += 1
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left == -1 or right == -1:
            self.res += 1
            return 1

        # 如果左右子节点有一个有相机，那么当前节点就不需要相机了，否则返回一个没有相机的标记
        if left == 1 or right == 1:
            return 0
        else:
            return -1
