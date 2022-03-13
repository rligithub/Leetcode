# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.dfs(robot, 0, 0, 0, direction, set())

    def dfs(self, robot, i, j, dire, direction, visited):
        visited.add((i, j))
        robot.clean()

        for k in range(4):
            new_dire = (dire + k) % 4
            dx, dy = direction[new_dire]
            x = i + dx
            y = j + dy
            if (x, y) not in visited and robot.move():  # movable
                self.dfs(robot, x, y, new_dire, direction, visited)
                # backtrack to prev step
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            # turn diff direction --> dire + +
            robot.turnLeft()







