# WordleSolver

### Task Definition
The player has 5 chances to guess the word.

Once a guess, the player can get the feedback of his attempt.

- If the letter was dyed green, it means the letter is in the correct place in the answer.

- If the letter was dyed yellow, it means the letter is included in the answer, but in a wrong place.

- If the letter was dyed black, it means the letter is not included in the answer.

The player must make full use of the feedback, and adjust his strategy to try next time, 
until he guesses the right word in a limited chance.

Example:

![avatar](/Resource/fig/README/wordle_example.png)

More info:

1. https://en.wikipedia.org/wiki/Wordle
2. https://www.nytimes.com/games/wordle/index.html
3. https://www.cnet.com/culture/internet/wordle-everything-to-know-about-the-viral-word-game/

### Features of Version 1.0

1. Set correct answer and the first attempt
2. Get feedbacks and select next candidate according to known information
3. Continue to try until bingo or exceed the max limit

```text
initial word candidates loaded, length: 9972
============================================================
Try [ spark ] this time
green: {0: 's', 1: '#', 2: '#', 3: '#', 4: '#'}
yellow: {}
black: {'r', 'p', 'a', 'k'}
After black selection, length of candidates: 5704
After green selection, length of candidates: 724
After yellow selection, length of candidates: 724
============================================================
Try [ socle ] this time
green: {0: 's', 1: '#', 2: '#', 3: '#', 4: '#'}
yellow: {'o': [1]}
black: {'e', 'l', 'r', 'p', 'k', 'c', 'a'}
After black selection, length of candidates: 389
After green selection, length of candidates: 389
After yellow selection, length of candidates: 220
============================================================
Try [ suing ] this time
green: {0: 's', 1: '#', 2: '#', 3: '#', 4: '#'}
yellow: {'o': [1], 'n': [3]}
black: {'e', 'l', 'u', 'r', 'p', 'k', 'c', 'g', 'i', 'a'}
After black selection, length of candidates: 115
After green selection, length of candidates: 115
After yellow selection, length of candidates: 61
============================================================
Try [ sposh ] this time
green: {0: 's', 1: '#', 2: 'o', 3: '#', 4: '#'}
yellow: {'o': [1], 'n': [3], 's': [3], 'h': [4]}
black: {'e', 'l', 'u', 'r', 'p', 'k', 'c', 'g', 'i', 'a'}
After black selection, length of candidates: 34
After green selection, length of candidates: 21
After yellow selection, length of candidates: 11
============================================================
Try [ shown ] this time
Bingo! Congratulations!
Total attempts: 4
```

### To-Do

- [ ] More optimization of v1.0
- [ ] Allow user to interact with WordleSolver v1.0
- [ ] Experiment to calculate the accuracy of v1.0
- [ ] How about using a regex to do a window matching?
- [ ] Visualization of process
- [ ] Statistics of guess
- [ ] Build interface to interact with https://www.nytimes.com/games/wordle/index.html
