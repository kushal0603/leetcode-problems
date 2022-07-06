class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1

        for i in range(2, n+1):
            if i % 2 == 0: a = a + b
            else: b = a + b
                
        return (a, b)[n%2 != 0]