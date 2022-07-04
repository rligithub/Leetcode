class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for file in path.split("/"):

            if file == "..":
                if stack:
                    stack.pop()
            elif file == "." or not file:
                continue
            else:
                stack.append(file)

        res = "/" + "/".join(stack)
        return res