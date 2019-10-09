# WaffleWords2
A Python program for finding waffle words.

wafflewords.py takes as input an integer, N, and outputs "waffle words" that are of length N. Waffle words have the following qualities:

1. They are words that can be found in a dictionary (e.g., a text file, such as the one provided, which contain a list of words). 
2. If you choose the right letter to remove from a waffle word, the resulting substring will also be a waffle word. The letter that is removed can be at any location in the waffle word.
3. When a substring of length 1 is reached, the substring must be one of the three one-letter English words, a, i, or o. 

wafflewords.py was inspired by the following riddle from Quora (source below): 
What eight letter word can have a letter taken away and it still makes a word? Take another letter away and it still makes a word. Keep on doing that until you have one letter left. What is that word?

In a separate file called "waffle-words-length-8" I have listed 1844 waffle words that are solutions to this riddle. 



## How wafflewords.py works
wafflewords.py iterates through all dictionary words of the input length, and tests the word using the function testwaffleword. In this function, the word to be tested, word_to_test, is partitioned into substrings of length one less than word_to_test. If any of these substrings, test_word, are English words that have not yet been tested for inclusion as waffle words, then they are tested by a recursive call to testwaffleword. If none of the substrings are waffle words, then word_to_test is not a waffle word. If the substring is a waffle word, then word_to_test is a waffle word.

Using a dictionary to store whether a string is a waffle word means that substrings of a string that has been found to be a waffle word (or not be a waffle word) need not be retested. 
  


## Usage
wafflewords.py requires a dictionary of English words that is read and added to "words_by_length", a dictionary data structure created during the execution of the program. words_by_length is a list of N python dictionaries, where N is the user-provided input. Each dictionary at position (N-1) contains all the words of length N that were found in the dictionary of English words as keys. The keys have one of the following three values:

	U = "unseen", words in the dictionary at position (N-1) that have not yet been seen (i.e., that have not been tested to be waffle words). 
	Y = "yes", words that are waffle words. 
	N = "no", words that are not waffle words. 

wafflewords.py looks, in the same directory as the program, for a text file called "english-words.txt". The program uses the words in this text file to populate words_by_length. 



## Comparison to WaffleWords.java
WaffleWords.java was my first approach to finding waffle words. That program uses a brute-force method that involves the following steps: 

1. Starting from single-letter waffle words, append each letter of the alphabet to the single-letter waffle word to form a new string. 
2. Test the resulting new string to see if it's a waffle word (i.e., search for the new string in a dictionary data structure that contains English words). If the new string is a waffle word, then add it to a list of waffle words. 
3. Test the strings that were added to the list of waffle words by appending each letter of the alphabet to the string at each position of the string (since any position in a waffle word is a valid position to remove a letter). 
4. Repeat steps 2 and 3 until waffle words of the input length are found. 

Drawbacks of the above algorithm include that some words will be tested more than once. To combat this, WaffleWords.java includes a list of words that were tested and found to not be waffle words. However, as the list of "failed" words grows, it becomes less advantageous to continually check the reject list. 

wafflewords.py is an improvement on the above algorithm as it implements a "top-down" dynamic programming approach in which words of the input length are tested, and when the word or a substring is found to not be a waffle word, the algorithm does not check subsequent shorter-length substrings. This information is also stored for future use in the dictionary in the form of the "N" value.   



## Note on Intellectual Property

I do not own the dictionary text file "english-words.txt". I found this text file online. You can find the source (ENGLISH - 194,000 words) by following the link below. 

Find english-words.txt here:
<http://www.gwicks.net/dictionaries.htm>

Find Quora riddle here:
<https://www.quora.com/What-eight-letter-word-can-have-a-letter-taken-away-and-it-still-makes-a-word-Take-another-letter-away-and-it-still-makes-a-word-Keep-on-doing-that-until-you-have-one-letter-left-What-is-that-word>
