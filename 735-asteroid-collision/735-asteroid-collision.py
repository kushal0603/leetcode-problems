class Solution:
	def asteroidCollision(self, asteroids: List[int]) -> List[int]:
		if all( asteroids[i] > 0 for i in range(len(asteroids))): return asteroids
		if all( asteroids[i] < 0 for i in range(len(asteroids))): return asteroids
		if not asteroids: return asteroids
		n = len(asteroids)
		j = 0
		while asteroids[j] < 0: j += 1
		while j < n and asteroids[j] > 0: j += 1
		if j == n: return asteroids

		i = 0
		while i + 1 < n:
			if asteroids[i] < 0: 
				i += 1
				continue
			if asteroids[i] > 0 and asteroids[i+1] < 0:
				if asteroids[i] > abs(asteroids[i+1]):
					return self.asteroidCollision(asteroids[:i+1] + asteroids[i+2:])
				elif abs(asteroids[i+1]) > asteroids[i]:
					return self.asteroidCollision(asteroids[:i] + asteroids[i+1:])
				else: return self.asteroidCollision(asteroids[:i] + asteroids[i+2:])
			i += 1