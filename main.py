from init import initial_candidates

# set params here
max_try = 5          # the max numbers of attempts can be made
has_tried = 0        # the number of attempts have been made
this_try = "spark"   # the word currently used for the attempt
correct = 'chunk'    # the correct answer
candidates = set()   # alternative words

feedback = {"green": dict(),    # index: letter. The correct letter in correct index
            "yellow": set(),    # TODO: use dict
            "black": set()}     # set of incorrect letters


def try_answer() -> bool:
    """
    1. compare the current candidate and get feedback
    2. select and update next candidate

    :return: True if right answer else False
    """
    global this_try
    print("=" * 60)
    print("Try", this_try, "this time")

    if this_try == correct:
        print("Bingo! Congratulations!")
        return True

    compare()
    this_try = select_candidate()

    return False


def compare():
    """
    iterate each letter in the word and compare it with the correct answer
    categorize and record each letter
    1. letter not in answer:                      [black]
    2. letter in answer but not in correct index: [yellow]
    3. letter in answer and in correct index:     [green]

    :return: Nothing but update global feedback in the process
    """
    global feedback
    for index, letter in enumerate(this_try):
        if letter not in correct:  # black
            feedback["black"].add(letter)
        elif letter in correct and correct[index] != this_try[index]:  # yellow
            feedback["yellow"].add(letter)
        elif correct[index] == this_try[index]:  # green
            feedback["green"][index] = letter
    print("Green:", feedback["green"])
    print("Yellow:", feedback["yellow"])
    print("Black:", feedback["black"])


def select_candidate():
    """
    update candidates according to global feedback
    1. initial selection: if the candidates list is empty, select matching words from initial_candidates
    2. green selection:   remove words with letters in incorrect index  # todo: add more matching words
    3. black selection:   remove words with wrong letters
    4. yellow selection:  remove words with wrong letters  # todo:remove right letters in wrong index

    :return: the first candidate in the list of candidates
    """
    global candidates
    candidates = list(candidates)  # convert set into list, for iterating
    # 1. initial selection
    if len(candidates) == 0:
        for candidate in initial_candidates:
            flag = 1
            for key in feedback["green"].keys():
                if candidate[key] != feedback["green"][key]:
                    flag = 0
                    break
            if flag:
                candidates.append(candidate)
        print("After initial selection, length of candidates:", len(candidates))
    # 2. green selection
    if len(feedback["green"].keys()) > 0:
        for candidate in candidates:
            for key in feedback["green"].keys():
                if candidate[key] != feedback["green"][key]:
                    candidates.remove(candidate)
                    break
    print("After green selection, length of candidates:", len(candidates))
    # 3. black selection
    if len(feedback["black"]) > 0:
        black_chars = list(feedback["black"])

        for candidate in candidates:
            for char in black_chars:
                if char in candidate:
                    # print(char, "in", candidate)
                    candidates.remove(candidate)
                    break

    print("After black selection, length of candidates:", len(candidates))

    # 4. yellow selection
    if len(feedback["yellow"]) > 0:
        yellow_chars = list(feedback["yellow"])

        for candidate in candidates:
            for char in yellow_chars:
                if char not in candidate:
                    candidates.remove(candidate)
                    break

    print("After yellow selection, length of candidates:", len(candidates))

    return candidates[0]


if __name__ == '__main__':
    # loop
    while has_tried < max_try:
        if try_answer():
            break
        # counter
        has_tried += 1

    print("has tried:", has_tried)
