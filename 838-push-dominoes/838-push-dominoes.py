import re

def _domino_replace(match_obj: re.Match) -> str:
	s = match_obj.group(0)
	match (s[0], s[-1]):
		case ('R', 'L'): # meet in the middle
			half = len(s) // 2
			if len(s) % 2:
				return f"{'R' * half}.{'L' * half}"
			return f"{'R' * half}{'L' * half}"
		case ('R', _): # right propagates
			return 'R' * len(s)
		case (_, 'L'): # left propagates
			return 'L' * len(s)
		case _: # no change
			return s

class Solution:
	def pushDominoes(self, dominoes: str) -> str:
		return re.sub(r"R?\.+L?", _domino_replace, dominoes)