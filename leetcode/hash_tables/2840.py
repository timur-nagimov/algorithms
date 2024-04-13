class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a_chet = []
        a_nechet = []

        b_chet = []
        b_nechet = []

        for i in range(len(s1)):
            if i % 2 == 0:
                a_chet.append(s1[i])
            else:
                a_nechet.append(s1[i])

        for i in range(len(s2)):
            if i % 2 == 0:
                b_chet.append(s2[i])
            else:
                b_nechet.append(s2[i])

        a_chet.sort()
        a_nechet.sort()
        b_chet.sort()
        b_nechet.sort()

        if a_chet == b_chet and a_nechet == b_nechet:
            return True
        return False
