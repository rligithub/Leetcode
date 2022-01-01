class Solution1:
    def pathInZigZagTree(self, label: int) -> List[int]:

        res = []
        node_count = 1
        level = 1
        # get max level
        while label >= node_count * 2:
            node_count *= 2
            level += 1
        # Iterate from the target label to the root
        while label != 0:
            res.append(label)

            level_max = 2 ** (level) - 1
            level_min = 2 ** (level - 1)

            label = int((level_max + level_min - label) / 2)

            level -= 1

        return res[::-1]
