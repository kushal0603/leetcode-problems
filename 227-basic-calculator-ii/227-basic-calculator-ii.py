from math import ceil, floor


class Solution:
    def calculate(self, s: str) -> int:
        # trim spaces
        s = "".join(s.split())
        end = len(s)-1
        stk, num, ope = [], "", "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num += c
            if not c.isdigit() or i == end:
                num = int(num)
                if ope == "+":
                    stk.append(num)
                elif ope == "-":
                    stk.append(-num)
                elif ope == "*":
                    stk.append(stk.pop()*num)
                elif ope == "/":
                    num = floor(num) if (num := stk.pop()/num) > 0 else ceil(num)
                    stk.append(num)
                num, ope = "", c
        return sum(stk)