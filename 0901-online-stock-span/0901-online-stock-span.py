class StockSpanner:

    def __init__(self):
        self.st=[] # storing tuple of price and span (price,span)
        

    def next(self, price: int) -> int:
        span=1
        while self.st and price>=self.st[-1][0]:
            span+=self.st[-1][1]
            self.st.pop()
        self.st.append((price,span))
        
        return span