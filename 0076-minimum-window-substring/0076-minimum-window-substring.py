class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        window, need = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for ch in t: need[ch] += 1
        
        valid = 0
        res = ""
        
        l, r = 0, 0 # [l, r)
        while r < len(s):
            ch = s[r]
            r += 1
            
            if ch in need:
                window[ch] += 1
                if window[ch] == need[ch]:
                    valid += 1
            
			# keep finding minimum valid substring
            while valid == len(need):
                if res == "" or len(s[l:r]) < len(res):
                    res = s[l:r]
                    
                ch = s[l]
                l += 1
                if ch in need:
                    if window[ch] == need[ch]:
                        valid -= 1
                    window[ch] -= 1
        
        return res