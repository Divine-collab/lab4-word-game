**How to Run**
Ensure you have Python 3.x installed. Navigate to the project directory and run:

Bash
python3 main.py
🎮 How to Play
Select a Category: Choose from Food, Fruits, or CS Terms.

Select Difficulty:

Easy: 10 lives and a 20-second timer per guess.

Hard: 4 lives and a 10-second timer per guess.

Guess Letters: Enter one letter at a time.

Replay: After a win or loss, you will be prompted to play again to increase your total score.

Technical Implementation
This project follows strict software engineering constraints:

Loop-Free Logic: The entire game is built using Recursion. There are zero while or for loops in the source code.

Layered Separation:

Logic Layer: Pure functions handle state updates, word masking, and validation.

UI Layer: Manages terminal output and user input, keeping the "brain" of the code separate from the interface.

Persistent State: The score is passed through the recursive stack to allow for a continuous gaming session.


Testing
To verify the logic layers (Validation and State Updates), you can run the unit tests (if applicable):

Bash
python3 -m unittest test_game.py