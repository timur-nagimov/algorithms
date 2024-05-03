class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_isomorphia = {}
        t_isomorphia = {}

        for i in range(len(s)):
            if s[i] not in s_isomorphia:
                s_isomorphia[s[i]] = t[i]
            if t[i] not in t_isomorphia:
                t_isomorphia[t[i]] = s[i]

            if s_isomorphia[s[i]] != t[i] or t_isomorphia[t[i]] != s[i]:
                return False

        return True
