class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        n = len(s)

        if n != len(goal):
            return False

        else:

            for i in range(len(s)):
                if s==goal:
                    return True
                else:
                    s = s[1:n] + s[0]

        return False