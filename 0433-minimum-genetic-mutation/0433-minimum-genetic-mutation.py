class Solution(object):
    def dfs(self, current, end, mutations, remaining_bank):
        
        if current == end:
            return mutations
        
        if len(remaining_bank) == 0:
            return -1
        
        mutation_list = []
        for gene in remaining_bank:
            genes_separated = sum([gene[i] != current[i] for i in range(len(gene))])
            if genes_separated == 1:
                sep_mutations = self.dfs(gene, end, mutations + 1 , [i for i in remaining_bank if i != gene])
                if sep_mutations != -1:
                    mutation_list.append(sep_mutations)
                    
        return min(mutation_list) if len(mutation_list) != 0 else -1
        
    def minMutation(self, start, end, bank):
        mutations = self.dfs(start, end, 0, bank)
  
        return mutations