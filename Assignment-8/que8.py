class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        ns = len(s)
        ng = len(goal)

        if ns != ng:
            return False

        if s == goal:
            farr = [0] * 26
            for ch in s:
                farr[ord(ch) - ord('a')] += 1
            
            for count in farr:
                if count > 1:
                    return True
            
            return False

        ans = []
        for i in range(ns):
            if s[i] != goal[i]:
                ans.append(i)
                if len(ans) > 2:
                    return False

        return len(ans) == 2 and s[ans[0]] == goal[ans[1]] and s[ans[1]] == goal[ans[0]]