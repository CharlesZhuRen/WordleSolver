from init import initial_candidates, alphabets

# set params here
max_try = 5
has_tried = 0
this_try = "spark"
correct = 'chunk'
candidates = []

feedback = {"green": dict(),
            "yellow": set(),
            "black": set()}


def try_answer() -> bool:
    """
    1. compare the current candidate and get feedback
    2. select next candidate
    :return: True if right answer else False
    """
    global this_try
    print(this_try)
    if this_try == correct:
        return True

    compare()
    this_try = select_candidate()
    print("-----------------------")
    return False


def compare():
    global feedback
    for index, letter in enumerate(this_try):
        if letter not in correct:  # black
            feedback["black"].add(letter)
        elif letter in correct and correct[index] != this_try[index]:  # yellow
            feedback["yellow"].add(letter)
        elif correct[index] == this_try[index]:  # green
            feedback["green"][index] = letter
    print(feedback)


def select_candidate():
    # green: char in right place
    # yellow: char in word
    # black: char not in word
    global candidates
    # first selection: select those contain green char in right place
    if len(feedback["green"].keys()) > 0:
        if len(candidates) == 0:
            for candidate in initial_candidates:
                flag = 1
                for key in feedback["green"].keys():
                    if candidate[key] != feedback["green"][key]:
                        flag = 0
                        break
                if flag:
                    candidates.append(candidate)
        else:
            for candidate in candidates:
                for key in feedback["green"].keys():
                    if candidate[key] != feedback["green"][key]:
                        candidates.remove(candidate)
                        break
    print("Green: length of candidates:", len(candidates))
    # second selection: remove those which contain black char
    if len(feedback["black"]) > 0:
        black_chars = list(feedback["black"])

        for candidate in candidates:
            for char in black_chars:
                if char in candidate:
                    print(char, "in", candidate)
                    candidates.remove(candidate)
                    break

    print("Black: length of candidates:", len(candidates))

    # last selection: select those which contain yellow char
    if len(feedback["yellow"]) > 0:
        yellow_chars = list(feedback["yellow"])

        for candidate in candidates:
            for char in yellow_chars:
                if char not in candidate:
                    candidates.remove(candidate)
                    break

    print("Yellow: length of candidates:", len(candidates))

    candidates = list(set(candidates))

    return candidates[0]


if __name__ == '__main__':
    # loop
    while has_tried < max_try:
        if try_answer():
            break
        # counter
        has_tried += 1

    print("has tried:", has_tried)
