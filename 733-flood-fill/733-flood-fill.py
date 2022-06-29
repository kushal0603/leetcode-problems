class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
		if image == None:
			return 
		current_color = image[sr][sc]
		height = len(image)
		weight = len(image[0])

		def dfs(sr, sc):
			if 0 <= sc < weight and 0 <= sr < height and image[sr][sc] == current_color and image[sr][sc] != newColor :
				image[sr][sc] = newColor
				dfs(sr + 1, sc)
				dfs(sr - 1, sc)
				dfs(sr, sc -1)
				dfs(sr, sc + 1)


		dfs(sr, sc)
		return image