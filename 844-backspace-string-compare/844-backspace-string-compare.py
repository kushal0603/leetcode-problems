def word_op(string: str) -> list[str]:
    stack = []
    for char in string:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return stack

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st_s = word_op(s)
        st_t = word_op(t)
        if len(st_s) != len(st_t):
            return False
        return all(char_s == char_t for char_s, char_t in zip(st_s, st_t))