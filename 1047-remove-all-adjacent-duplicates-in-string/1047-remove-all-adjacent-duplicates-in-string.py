class Solution:
    def removeDuplicates(self, s: str) -> str:
        if s == "":
            return ""
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                stack.pop(-1)
            else:
                stack.append(s[i])
        return "".join(stack)