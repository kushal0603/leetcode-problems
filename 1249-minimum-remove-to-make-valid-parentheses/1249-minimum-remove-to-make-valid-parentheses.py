class Solution:
    def minRemoveToMakeValid(self, s):
        stack, s_list = [], list(s)
        for i, char in enumerate(s):
            if stack and stack[-1][0] == '(' and char == ')':
                stack.pop(-1)
            else:
                if char in ['(',')']:
                    stack.append((char,i))
        for _,ind in stack:
            s_list[ind] = ''
        return ''.join(s_list)