class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans=[0]*len(grid[0])
        for b in range(0,len(grid[0])):
            i=0
            j=b
            while(1):
                if(j==len(grid[0])-1 and grid[i][j]==1):
                    ans[b]=-1
                    break
                elif((grid[i][j]==1 and grid[i][j+1]==-1)or(grid[i][j]==-1 and grid[i][j-1]==1)):
                    ans[b]=-1
                    break
                elif(grid[i][j]==-1 and j==0):
                    ans[b]=-1
                    break
                else:
                    if(grid[i][j]==1):
                        j+=1
                    else:
                        j-=1
                    i+=1
                    if(i>=len(grid)):
                        ans[b]=j
                        break
        return ans