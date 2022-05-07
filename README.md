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
2. Get feedbacks and select next candidate
3. Continue to try until bingo or exceed the max limit

### To-Do
1. Make full use of updated Green information
2. Make full use of updated Yellow information
3. Set correct answer and choose the initial attempt automatically
4. Visualization of process
5. Statistics of guess
6. Build interface to interact with https://www.nytimes.com/games/wordle/index.html
