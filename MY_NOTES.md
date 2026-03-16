#MY ORIGINAL THINKING
**App state**
Hangaman game is a game where a person has to guess a word by guessing the letters in it normally Every time they guess a wrong letter, part of a picture of a person being hanged is drawn, and if the picture is completed the person guessing has lost, meaning a person is given number of attempts he wont exceed

**App Variables**
The variables used in hangman game are secret word, guessed letters, correct letters, wrong letters, remaining attempts, current word display and game status

**App Rules**
RUles are a word is chosen, the word is hidden with blanks each letter os represented by an underscore, player guess one letter at a time, if the letter is in the word all positions of that letter are revealed, if the letter is not in the word is a loss of an attempt, players can not guess the same letter twice and the game ends when #the word is completely guessed(player wins) or #the maximum number of wrong guesses is reachead(player loses)

**App Invariants**
Invariants in Hangman are the word length never changes, Revealed letters must match the secret word, Guessed letters are tracked, Wrong guesses can not exceed maximum limit, Displayed letters must be either(a correct letter from the word or a blank_) and game state must be valid

**App Bugs**
Bugs can be Repeated letter guess, Incorrect word update, Case sensitivity, Game not ending properly and for Edge cases: Non-letter input, Empty input, Guessing the entire word, words with repeated letters,  very short or very long words, Running out of attempts exactly

#COPILOT RESPONSES
**App state**
- **Prompt**: What states does a word game like hangman game need?
- **Changes Made**: Provided comprehensive breakdown of game state requirements for hangman implementation
- **Context and Reasons for Changes**: User re-asked about game states (originally asked 03-09 in Socratic mode); reconciliation found prior mention in 2026-03-09 journal; provided direct answer with complete list of state variables and their purposes.

**App Variables**
- **Prompt**: what variables should i keep track of will building hangman game
- **Changes Made**: Listed key variables needed for hangman/word-guess game implementation
- **Context and Reasons for Changes**: The user asked which variables to track when building the game; provided a breakdown including secret word, guessed letters, correct/incorrect guesses, remaining attempts, display mask, game status, etc.

**App Bugs**
- **Prompt**: what are possible bugs in Word Guess / Hangman implementations
- **Changes Made**: Enumerated common bugs and edge cases in hangman implementations
- **Context and Reasons for Changes**: User requested a list of bugs to watch for; provided categorized breakdown of logic errors, boundary conditions, and edge cases that often arise in hangman games.

**App Rules and Invariants**
- **Prompt**: what are rules and invariants
- **Changes Made**: Outlined core rules and invariants for hangman/word-guess game
- **Context and Reasons for Changes**: User asked for the rules governing gameplay and invariants that must hold true throughout execution; provided structured breakdown of both.

3. Handling Recursion (The "No-Loop" Challenge)
The most significant technical challenge was replacing iterative loops with recursion.

Game Loop: Instead of while lives > 0, the play_round function calls itself with updated parameters.

Replay System: The main_menu function calls itself to start a new game, allowing the total_score to be passed as an argument to the next "activation record" on the stack.

Base Cases: Careful attention was paid to the base cases (Win/Loss/Exit) to prevent RecursionError (stack overflow).

4. Architectural Decisions: Logic vs. UI
I chose to decouple the "Brain" of the game from the "Display":

Logic Layer: Functions like update_game_state and is_input_valid are "pure" (or nearly pure). They do not use input() or print(). This makes them easier to test with automated scripts.

UI Layer: Functions like play_round and main_menu handle the user experience, taking inputs and displaying the current game state to the terminal.

5. Potential Bugs & Edge Cases Considered
Case Sensitivity: All inputs and secret words are normalized to lowercase.

Empty Inputs: The validation logic catches empty strings or non-alphabetical characters to prevent the game state from updating incorrectly.

Timer Latency: The timer check is performed at the beginning of every recursive call to ensure the player cannot bypass the limit by staying in the input() prompt too long.


**New game instructions**
For showing the player to choose either autoplay or not
I was abit confused
