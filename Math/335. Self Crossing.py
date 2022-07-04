class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        # 画图-->  三种情况：第1条和第4条相交，第1条和第5条相交，第1条和第6条相交

        for i in range(3, len(distance)):
            # case1： 第四条线与第一条线相交  (所有相隔三个的情况都通用)
            if distance[i - 1] <= distance[i - 3] and distance[i] >= distance[i - 2]:
                return True
                # case2： 第五条线与第一条线相交 （所有相隔四个的情况都通用）
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True
                # case3： 第六条线与第一条线相交 （所有相隔五个的情况都通用）
            if i >= 5 and distance[i - 1] + distance[i - 5] >= distance[i - 3] and distance[i - 1] <= distance[
                i - 3] and distance[i - 2] > distance[i - 4] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True

        return False