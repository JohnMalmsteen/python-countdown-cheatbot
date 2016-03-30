# Countdown Words Game Solver
Python project to return the longest OED word from 9 random letters, modeling as many of the countdown rules as possible

![countdown](http://www.gtigazette.com/wp-content/uploads/2015/02/120521_britishgames_countdown_titlecard.jpg "countdown")

Contents:
---------
1. About
2. Word List
3. Algorithm
4. Extras

1 - About
---
This repo contains my solution for the Theory of Algorithms module (Dr. Ian McLoughlin) CA project.

The aim of this project is to produce code that solves the Countdown 'Letters Game' in which players select 9 letters from two stacks: vowels and consonants. The letters in the stack are frequency weighted in relation to their frequency of occurrence in the English language.

The player must select a minimum of 3 vowels and 4 consonants. Having select the 9 letters the players must then come up with the longest word they can made up from the 9 letters with no repetition of letters (unless those letters are repeated in the 9 letters in play)

The players are limited to the words in the Oxford English Dictionary with some extra words allowed:

>Standard inflections of nouns and verbs—for example, escapes, escaped and escaping—are accepted even though not explicitly shown in the dictionary. Comparative and superlative forms of monosyllabic adjectives—for example, greater and greatest—are valid although these too are not explicitly shown. For longer adjectives, the inflections must be stated explicitly.[48] However, some words given in the dictionary are not permitted: proper nouns (Kurdistan), hyphenated words (re-embark), some plurals of mass nouns (mankinds), and words that occur only in combination—for example, mistle is invalid as it is used only in mistle thrush. Also, only British spelling is permitted—American spellings and inflections, such as flavor and signaled, are invalid.

[Source](https://en.wikipedia.org/wiki/Countdown_(game_show))

2 - Word List
---
The word list I used is the "Moby Word Lists by Grady Ward" which I have had for a while and I'm not sure where I got it from (I think it might be packaged with Kali Linux). I was going to use the /usr/share/dict/words list that exists on OSX (and almost all linux distribution) but I found it to be a bit limited compared to the Moby List.

The Moby list is available [here](http://www.gutenberg.org/files/3201/files/ "Moby Word List"), although this is not the exact version that I have. The particular file that I am using is the 354,984 single words list.

I strip the list of any words that are shorter than 4 (as that is one of the rules of countdown) and greater than 9, I also remove any word that has a capital first letter as it is a proper noun, and any word that has non alphabetical characters such as hyphens or apostrophes.

3 - Algorithm
---
My approach is to pre-process the dictionary which then allows for O(1) access for future lookups.

As the words list is processed I sort the letters of each word into alphabetical order and then use this sorted string as the key in a dict() whose value is a set of words which are anagrams of that sorted key.

When a word must be tested for anagrams it is only required to sort the letters into alphabetical order and then look it up in the dictionary. To do this sorting I am using the in-built sorted(iterable) function which produces a sorted list from an iterable (ie. string in this case) and then joining that list back into a string afterwards.

The sort algorithm used by python here is Timsort which is a stable (the output element order will always be the same for the same input elements) sorting algorithm based on merge sort and insertion sort and it takes advantage of 'runs' of already sorted elements that occur in natural data. For this reason I put the vowels at the start of my randomly generated 9 letter strings since that would give the statistical best chance for runs of sorted letters (speed stripes and massaging the engine with tiger blood). Regardless, the worst case for this sort is O(N(log(N))) and N max is 9.

Should there not be a nine letter anagram in the dictionary for our random letters then it is required to try and find an 8 letter anagram and failing that, 7 and so on and so forth.

Since these substrings are to be sorted it is only required that the combinations of the letters be produced. For any given 9 letter string given the maximum number of combinations that must be checked against the dictionary is C(9, 9) + C(9, 8) + C(9, 7) + C(9, 6) + C(9, 5) + C(9, 4) = 381 although it is rare that an anagram isn't found before length 6 and 252 of these combinations are at lengths 4 and 5. Since we are looking for the largest anagram it obviously makes sense to start from the longest combination and work down.

To produce these combinations I used [itertools.combinations(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations)

4 - Extras
---
I got tired of not knowing what any of the words meant so I threw in a function that queries a rest API to try and find the definition, I found that even then a lot of the words were not known on that API so I suppose their dictionary isn't that extensive.

The API I used is located [here](dictionaryapi.net)

5 - Testing
---
Running the timeit function 10,000 on the find_largest_anagram() feeding it in the randomly generated 9 letter strings takes .68 seconds, so one solution takes about .000068 seconds although obviously this does not call the rest API and the pre-processing is done in advance.

<a href="https://github.com/JohnMalmsteen"><img src="https://avatars1.githubusercontent.com/u/7085486?v=3&s=400" width="100px" height="100px" title="John" alt="John Image"/></a>
