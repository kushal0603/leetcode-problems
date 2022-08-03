class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        visited = []
        first_time = True
        while num != str(n) or first_time:
            final_num = 0
            for i in num:
                final_num += int(i) ** 2
            print(final_num)
            if final_num in visited:
                break
            visited.append(final_num)
            if final_num == 1: 
                return True
            num = str(final_num)
            first_time = False
        return False