import random
import time

# ==========================================
# LOGIC LAYER
# ==========================================

CATEGORIES = {
    "Fruits": ["apple", "mangoes", "grapes", "banana"],
    "Food": ["chicken", "tomatoes", "pasta", "pizza"],
    "CS Terms": ["python", "variable", "binary", "recursion"]
}

DIFFICULTY = {
    "1": {"name": "Easy", "lives": 10, "timer": 20},
    "2": {"name": "Hard", "lives": 4, "timer": 10}
}
CHOICE = {
    "You": {"name": "you are the one playing"}
    "Auto": {"name": "the autoplay"}
}


def get_masked_word(secret_word, guessed_letters):
    return [l if l in guessed_letters else "_" for l in secret_word]

def update_game_state(secret_word, guessed_letters, guess, lives):
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    if guess not in secret_word:
        lives -= 1
    is_won = all(letter in guessed_letters for letter in secret_word)
    return guessed_letters, lives, is_won

# ==========================================
# UI LAYER
# ==========================================

def play_round(secret_word, guessed_letters, lives, score, start_time, time_limit):
    """Recursive loop with score and timer tracking."""
    elapsed_time = time.time() - start_time
    
    # 1. Check Lose Condition (Lives or Timer)
    if lives <= 0:
        print(f"\nGame Over! Out of lives. The word was: {secret_word}")
        return score
    
    if elapsed_time > time_limit:
        print(f"\nTime's up! You took {int(elapsed_time)}s. The word was: {secret_word}")
        return score

    # 2. Display State
    display = get_masked_word(secret_word, guessed_letters)
    print(f"\nCategory: {category_name} | Timer: {int(time_limit - elapsed_time)}s")
    print(f"Word: {' '.join(display)} | Lives: {lives} | Current Score: {score}")

    guess = input("Guess a letter: ").lower()

    # 3. Basic Input Validation
    if not guess or not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
        print("Invalid or repeated guess. Try again.")
        return play_round(secret_word, guessed_letters, lives, score, start_time, time_limit)

    # 4. Update Logic
    guessed_letters, lives, is_won = update_game_state(secret_word, guessed_letters, guess, lives)

    if is_won:
        print(f"\nCongratulations! You guessed it: {secret_word}")
        return score + 1
    else:
        return play_round(secret_word, guessed_letters, lives, score, start_time, time_limit)

def main_menu(total_score=0):
    """The entry point that manages Categories, Difficulty, and Replay."""
    print("\n--- GUESS THE WORD: PRO EDITION ---")
    
    # Extension: Categories
    print(f"Categories: {', '.join(CATEGORIES.keys())}")
    cat_choice = input("Pick a category: ").title()
    global category_name # Simple way to show category in play_round
    category_name = cat_choice if cat_choice in CATEGORIES else "Food"
    
    # Extension: Difficulty
    print("Difficulties: 1 (Easy - 10 lives/20s), 2 (Hard - 4 lives/10s)")
    diff_choice = input("Select difficulty (1/2): ")
    settings = DIFFICULTY.get(diff_choice, DIFFICULTY["1"])

    # Setup Game
    word = random.choice(CATEGORIES[category_name])
    
    # Extension: Score system across multiple games
    new_score = play_round(word, [], settings["lives"], total_score, time.time(), settings["timer"])
    
    print(f"--- TOTAL SCORE: {new_score} ---")
    
    # Extension: Replay
    if input("\nPlay another round? (y/n): ").lower() == 'y':
        main_menu(new_score)
    else:
        print(f"Final Score: {new_score}. Goodbye!")

if __name__ == "__main__":
    main_menu()