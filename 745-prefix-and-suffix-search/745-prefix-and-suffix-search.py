class WordFilter:

	def __init__(self, words: List[str]):

		self.pair_suffix_prefix = {}

		for index in range(len(words)):

			for j in range(len(words[index])):

				new_word1 = words[index][:j+1]

				for k in range(len(words[index])):
					new_word2 = new_word1+'.'+words[index][k:]

					self.pair_suffix_prefix[new_word2] = index


	def f(self, prefix: str, suffix: str) -> int:

		search_word = prefix+'.'+suffix

		if search_word in self.pair_suffix_prefix:
			return self.pair_suffix_prefix[search_word]
		else:
			return -1