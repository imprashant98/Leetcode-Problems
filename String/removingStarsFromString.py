class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if i == '*' and len(st) > 0:
                st.pop()
            else:
                st.append(i)

        ans = ''.join(st)
        return ans
