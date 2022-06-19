class Solution:
    def suggestedProducts(self, products: List[str], searchword: str) -> List[List[str]]:
        res = []
        prefixes = {}
        products.sort()
        for i,word in enumerate(products):
            for j in range(0,len(word)):
                if word[:j+1] in prefixes:
                    prefixes[word[:j+1]].append(i)
                else:
                     prefixes[word[:j+1]] = [i]
        for i in range(0,len(searchword)):
            temp=[]
            ptrn = searchword[:i+1]
            if ptrn in prefixes:
                for j in prefixes[ptrn][:3]:
                    temp.append(products[j])
            res.append(temp)
        return res