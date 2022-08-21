class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def is_match(s, t):
            return all([sc==tc for (sc, tc) in zip(s, t) if tc!='*']) and any([tc!='*' for tc in t])
        def do_replace(t, i):
            return t[:i] + '*'*len(stamp) + t[(i+len(stamp)):]
        res = []
        while True:
            flag = False
            k = 0
            while k <= len(target)-len(stamp):
                s, t = stamp, target[k:(k+len(stamp))]
                if is_match(s, t): 
                    flag = True
                    res.append(k)
                    target = do_replace(target, k)
                    k+=len(stamp)
                else:
                    k+=1
            if flag==False: break
        return res[::-1] if target.count('*')==len(target) else []