class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # A随机坐一个位置（假设是坐在B的位置上），B上来之后看到位置被占，本来可以找新位置但是他坚持让A让出它的位置，让A去找新位置 --> 谁去找新位置，probability上来说并不影响，所以最后变相相当于 A和Z之间的位置可能是被互换了（Z选择坐空出来的最后一个位置，或者选择让A滚蛋）1/2
        if n <= 1:
            return 1
        else:
            return 0.5