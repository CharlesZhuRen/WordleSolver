from nltk.corpus import words

word_list = words.words()
initial_candidates = [x.lower() for x in word_list if len(x) == 5]
initial_candidates = list(set(initial_candidates))
print("initial word candidates loaded, length:", len(initial_candidates))

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
print("alphabets loaded")

