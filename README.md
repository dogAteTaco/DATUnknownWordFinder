# Description
I created a Python script to find unknown, non-english or invalid words in a text file based on a list of valid words. I created it because I want to create a Tolkien Universe dictionary for a Kindle, and the ones I've find are very incomplete or I would have to script a tool that extracts data from some wiki.
The script filters out all the valid English words and create a list with every word that the script finds that is not on that English list and write it into a file with all the unknown words found. 
The application I'm most interested in is for fantasy books, especially ones with lots of characters, places and creatures like The Lord of the Rings, Dune, The Witcher or even Harry Potter.

# How to use

1. You'll need 2 things to create a list of words to start creating your dictionary:
  - A text while with words you want be taken as valid (one word per line). (Read the section *Word resources* to get the most complete English word list I've found)
  - A text file with the book, article or whatever document you want to find unknown words (needs to be a simple text file)

2. Next, you'll need to run 'createCatalogs.py' and give it the location of your file with valid words (dictionary). This will create multiple files that separates the words into multiple files to make the process faster name as 'acatalog', 'bcatalog' and so on.

3. Run 'detectNonValidWords.py' by giving it the location to your text file you want to find unknown words in and this will create a file with a text file with all the unique unknown words.

# Kindle plans
With a list of words and definitions the plan is to create a more complete dictionary I can use in my Kindle. I already managed to create a Kindle dictionary but I kept coming across places and characters with no definition on "A Dictionary of Tolkien" by David Day, so the plan is to find all the character names, places and creatures to add my own descriptions and be able to distribute them

# Word resources
The word list I'm currently using is found at https://github.com/dwyl/english-words/blob/master/words.txt
