"""
wafflewords.py 
 
wafflewords.py takes as input an integer and outputs "waffle words" that are the same length 
as that integer. Waffle words have the following qualities:
 
1. They are words that can be found in a dictionary (e.g., a text file that contains a list of 
newline seperated words). 
2. If you choose the right letter to remove from a waffle word, the resulting word will also be
a waffle word. The letter that is removed can be at any location in the waffle word.  
3. When a substring of length 1 is reached, the substring must be one of the three one-letter 
English words, a, i, or o. 
 
See README for more info.
  
Eli Epperson 
"""

def testwaffleword(words_by_length,word_to_test):

	# Base case - the only one-letter words in the English language are a, i, and o. Therefore, 
	# if word_to_test is one of these then return True. Otherwise, return False becuase if the
	# final substring of a word is not a, i, or o, the word is not a WW. 
	if len(word_to_test) == 1:
		if word_to_test == "a" or word_to_test == "i" or word_to_test == "o":
			return words_by_length, True 
		else:
			return words_by_length, False

	for y in range(len(word_to_test)):

		# The value of test_word will be the substrings of word_to_test, not all of which will
		# be English words.
		test_word = word_to_test[0 : y : ] + word_to_test[y + 1 : : ]
		
		# If test_word is not an English word, then it can't be a WW. In this case, the code in the
		# if/elif will not be reached.
		if words_by_length[len(test_word)-1].get(test_word) == "U":
			waffle = False
			words_by_length, waffle = testwaffleword(words_by_length, test_word)

			# If the value of waffle is True, then the substring test_word is a WW. Since
			# word_to_test is a valid English word, it too is a WW and is marked as such here.   
			if (waffle):
				words_by_length[len(word_to_test)-1][word_to_test] = "Y"
				# Return True when a WW is found to update the value of waffle when we recurse up. 
				return words_by_length, True

		# If test_word has already been seen and marked as a WW, then simply mark word_to_test as
		# a WW. 
		elif words_by_length[len(test_word)-1].get(test_word) == "Y":
			words_by_length[len(word_to_test)-1][word_to_test] = "Y"
			return words_by_length, True

	# If none of the substrings set as test_word are English words or if none of the substrings
	# are valid WWs then word_to_test is not a WW and should be marked as "N".
	words_by_length[len(word_to_test)-1][word_to_test] = "N"
	return words_by_length, False


def main():
	waffle_length = int(input("Enter the length of the waffle words to be found. "))
	waffle_words = []

	# Open and read the words of the dictionary text file into a list.
	file1 = open("english-words.txt","r") 
	lines = file1.read().splitlines()

	# Create a list to hold the dictionary words. The list at index i contains words of length i+1
	words_by_length = [None] * waffle_length

	# Populate the list words_by_length with empty dictionary data structures that will store the 
	# dictionary words.  
	# The values of the dictionary will be one of the following three values: U, Y, N
	# U = "unseen", words in the dictionary that have not yet been seen
	# Y = "yes", words that are waffle words 
	# N = "no", words that are not waffle words

	for x in range(waffle_length):
		words_by_length[x] = {}
	
	for word in lines:
		length_of_word = len(word)

		# Populate the list with words that are the same length or shorter than waffle length
		# because words longer than waffle_length cannot be WWs of that length. 
		if length_of_word <= waffle_length:
			words_by_length[length_of_word-1][word] = "U"


	# Iterate over all dictionary words of an input length, waffle_length 
	for word in words_by_length[waffle_length-1]:
	
		waffle = False
		words_by_length, waffle = testwaffleword(words_by_length, word)
		
		# If waffle is True, then word is a WW. Add it to the list of WWs. 
		if(waffle):
			waffle_words.append(word)

	print(waffle_words)
	print("\nFound %d waffle words of length %d." % (len(waffle_words), waffle_length))	

if __name__ == "__main__":
	main()