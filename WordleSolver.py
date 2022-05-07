from init import initial_candidates

class WordleSolver:

    def __init__(self):
        # set params here
        self.max_try = 5  # the max numbers of attempts can be made
        self.has_tried = 0  # the number of attempts have been made
        self.this_try = "spark"  # the word currently used for the attempt
        self.correct = 'shown'  # the correct answer
        self.candidates = set()  # alternative words
        self.feedback = {"green": dict(),  # index: letter. The correct letter in correct index
                         # "yellow": set(),    # TODO: use dict
                         "yellow": {0: [], 1: [], 2: [], 3: [], 4: []},  # index: [letters shouldn't appear here]
                         "black": set()}  # set of incorrect letters, these letters shouldn't be in the candidate

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
            if letter not in self.correct:  # black
                self.feedback["black"].add(letter)
            elif letter in self.correct and self.correct[index] != self.this_try[index]:  # yellow
                # feedback["yellow"].add(letter)
                self.feedback["yellow"][index].append(letter)
            elif self.correct[index] == self.this_try[index]:  # green
                self.feedback["green"][index] = letter

        print("Green:", self.feedback["green"])
        print("Yellow:", self.feedback["yellow"])
        print("Black:", self.feedback["black"])

    def select_candidate(self):
        """
        update candidates according to global feedback
        1. initial selection: if the candidates list is empty, select matching words from initial_candidates
        2. green selection:   remove words with letters in incorrect index
        # TODO: add more matching words i.e. how to make full use of updated Green information?
        3. black selection:   remove words with wrong letters
        4. yellow selection:  remove words with wrong letters  # TODO: remove right letters in wrong index

        :return: the first candidate in the list of candidates
        """
        candidates = list(self.candidates)  # convert set into list, for iterating
        # 1. initial selection according to the first feedback
        if len(candidates) == 0:
            for candidate in initial_candidates:
                flag = 1
                for key in self.feedback["green"].keys():
                    if candidate[key] != self.feedback["green"][key]:
                        flag = 0
                        break
                if flag:
                    candidates.append(candidate)
            print("After initial selection, length of candidates:", len(candidates))

        # 2. green selection
        if len(self.feedback["green"].keys()) > 0:

            for candidate in candidates:
                for key in self.feedback["green"].keys():
                    if candidate[key] != self.feedback["green"][key]:
                        candidates.remove(candidate)
                        break
        print("After green selection, length of candidates:", len(candidates))

        # 3. black selection
        # TODO: does it really work？
        if len(self.feedback["black"]) > 0:
            black_chars = list(self.feedback["black"])

            for candidate in candidates:
                for letter in candidate:
                    if letter in black_chars:
                        candidates.remove(candidate)
                        break

        print("After black selection, length of candidates:", len(candidates))

        # 4. yellow selection
        if len(self.feedback["yellow"]) > 0:
            # yellow_chars = list(feedback["yellow"])

            for candidate in candidates:
                for index, letter in enumerate(candidate):
                    if letter in self.feedback["yellow"][index]:
                        # if char not in candidate:
                        candidates.remove(candidate)
                        break

        print("After yellow selection, length of candidates:", len(candidates))

        return candidates[0]

    def run(self):
        # loop to try
        while self.has_tried < self.max_try:
            if self.try_answer():
                break
            # counter
            self.has_tried += 1

        if self.has_tried == 5:
            print("=" * 60)
            print("Sorry! You Lose!")