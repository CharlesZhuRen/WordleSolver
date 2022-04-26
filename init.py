from nltk.corpus import words

word_list = words.words()
initial_candidates = [x.lower() for x in word_list if len(x) == 5]
initial_candidates = list(set(initial_candidates))
print("initial word candidates loaded, length:", len(initial_candidates))
