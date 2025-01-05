import re


class Solver:

    def __init__(self):
        # set params here
        self.max_try = 5  # the max numbers of attempts can be made
        self.has_tried = 0  # the number of attempts have been made
        self.this_try = 'spark'  # the word currently used for the attempt
        self.correct = 'crash'  # the correct answer todo: random selection
        self.candidates = self.init_candidates()  # alternative words
        self.green = {0: '#', 1: '#', 2: '#', 3: '#', 4: '#'}  # index: letter in correct index
        self.yellow = dict()  # letter: [wrong place of letter]
        self.black = set()  # set of incorrect letters which shouldn't appear

    @staticmethod
    def init_candidates():
        with open("Resource/data/words.txt", "r") as f:
            initial_candidates = f.readlines()
            initial_candidates = [x.strip() for x in initial_candidates]
            print("loaded {} initial words".format(len(initial_candidates)))
            return initial_candidates

    def peep(self):
        print("green: {}\nyellow: {}\nblack: {}".format(self.green, self.yellow, self.black))

    def try_answer(self) -> bool:
        """
        1. compare the current candidate and get feedback
        2. select and update next candidate

        :return: True if right answer else False
        """

        print("=" * 60)
        print("Try [", self.this_try, "] this time")

        if self.this_try == self.correct:
            print("Bingo! Congratulations!")
            print("Total attempts:", self.has_tried)
            return True

        self.compare()
        self.candidates.remove(self.this_try)
        self.this_try = self.select_candidate()

        return False

    def compare(self):
        """
        iterate each letter in the word and compare it with the correct answer
        categorize and record each letter
        1. letter not in answer:                      [black]
        2. letter in answer but not in correct index: [yellow]
        3. letter in answer and in correct index:     [green]

        :return: Nothing but update global feedback in the process
        """
        for index, letter in enumerate(self.this_try):
            if letter not in self.correct:
                self.black.add(letter)
            elif self.correct[index] == self.this_try[index]:
                self.green[index] = letter
            elif letter in self.correct and self.correct[index] != self.this_try[index] and letter not in self.green:
                if letter in self.yellow:
                    self.yellow[letter].append(index)
                else:
                    self.yellow[letter] = [index]

        self.peep()

    def green_select(self, candidates):
        pattern = '^'
        for i in range(5):
            if self.green[i] != '#':
                pattern += self.green[i]
            else:
                pattern += '[a-zA-Z]'
        pattern += '$'

        regex = re.compile(pattern)

        target_words = [word for word in candidates if regex.match(word)]

        return target_words

    def select_candidate(self):
        """
        update candidates according to global feedback
        discrimination: black selection > green selection > yellow selection
        1. green selection:   select words with correct letter in right index
        2. black selection:   select words without incorrect letters
        3. yellow selection:  remove words with wrong letters

        :return: the first candidate in the list of candidates
        """
        candidates = list(self.candidates)  # convert set into list, for iterating

        # 1. black selection
        if len(self.black) > 0:

            for candidate in candidates:
                if set(candidate).intersection(self.black) != set():
                    candidates.remove(candidate)

        print("After black selection, length of candidates:", len(candidates))

        # 2. green selection
        if len(self.green.values()) > 1:
            candidates = self.green_select(candidates)

        print("After green selection, length of candidates:", len(candidates))

        # 3. yellow selection
        if len(self.yellow) > 0:
            # yellow_chars = list(feedback["yellow"])

            for candidate in candidates:
                flag = True
                # all yellow letters should appear
                for yellow_letter in self.yellow:
                    if yellow_letter not in candidate:
                        flag = False
                        break

                if not flag:
                    candidates.remove(candidate)
                    continue

                # all yellow letters shouldn't appear in an excluded index
                for index, letter in enumerate(candidate):
                    if letter in self.yellow and index in self.yellow[letter]:
                        candidates.remove(candidate)
                        break

        print("After yellow selection, length of candidates:", len(candidates))

        self.candidates = candidates

        return self.candidates[0] if len(self.candidates) > 0 else None

    def run(self):
        # loop to try
        while self.has_tried < self.max_try:
            if self.try_answer():
                break
            # counter
            self.has_tried += 1

        if self.has_tried == self.max_try:
            print("=" * 60)
            print("Sorry! You Lose!")
