class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if numRows == 1:
        #     return s
        
        # rows = [''] * numRows
        # row = 0
        # down = True
        
        # for ch in s:
        #     rows[row] += ch
            
        #     if down:
        #         if row == numRows - 1:
        #             down = False
        #             row -= 1
        #         else:
        #             row += 1
        #     else:
        #         if row == 0:
        #             down = True
        #             row += 1
        #         else:
        #             row -= 1
        
        # return ''.join(rows)
        t = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        r = [''] * numRows
        for i, char in enumerate (s) :
            r[t[i % len(t)]] += char
        return ''.join(r)