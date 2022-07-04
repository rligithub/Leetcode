# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # use rand7 to get rand49, then use rand49 to get rand10

        while True:
            row = rand7()
            col = rand7()

            random = (row - 1) * 7 + col
            if random <= 40:
                return (random - 1) % 10 + 1

