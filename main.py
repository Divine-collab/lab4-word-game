import random
import time

# ==========================================
# LOGIC LAYER
# ==========================================

CATEGORIES = {
    "Fruits": ["apple", "mangoes", "grapes", "banana"],
    "Food": ["chicken", "tomatoes", "pasta", "pizza"],
    "CS Terms": ["python", "variable", "binary", "recursion"],
}

DIFFICULTY = {
    "1": {"name": "Easy", "lives": 10, "timer": 20},
    "2": {"name": "Hard", "lives": 4, "timer": 10},
}

# Fixed syntax: added comma
CHOICES = {"1": "You", "2": "Auto"}


def get_masked_word(secret_word, guessed_letters):
    return [l if l in guessed_letters else "_" for l in secret_word]


def update_game_state(secret_word, guessed_letters, guess, lives):
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    if guess not in secret_word:
        lives -= 1
    is_won = all(letter in guessed_letters for letter in secret_word)
    return guessed_letters, lives, is_won


def get_auto_guess(guessed_letters):
    """Logic: Simple 'AI' that picks a random letter not yet guessed."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    available = [char for char in alphabet if char not in guessed_letters]
    return random.choice(available)


# ==========================================
# UI LAYER
# ==========================================


def play_round(
    secret_word, guessed_letters, lives, score, start_time, time_limit, mode="You"
):
    elapsed_time = time.time() - start_time

    if lives <= 0:
        print(f"\nGame Over! Out of lives. The word was: {secret_word}")
        return score

    if elapsed_time > time_limit:
        print(f"\nTime's up! The word was: {secret_word}")
        return score

    display = get_masked_word(secret_word, guessed_letters)
    print(
        f"\nMode: {mode} | Category: {category_name} | Timer: {int(time_limit - elapsed_time)}s"
    )
    print(f"Word: {' '.join(display)} | Lives: {lives} | Current Score: {score}")

    # Handling the Mode Choice
    if mode == "Auto":
        guess = get_auto_guess(guessed_letters)
        print(f"Autoplay guessed: {guess}")
        time.sleep(0.5)  # Small delay so it doesn't finish instantly
    else:
        guess = input("Guess a letter: ").lower()

    if not guess or not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
        if mode == "You":
            print("Invalid or repeated guess.")
        return play_round(
            secret_word, guessed_letters, lives, score, start_time, time_limit, mode
        )

    guessed_letters, lives, is_won = update_game_state(
        secret_word, guessed_letters, guess, lives
    )

    if is_won:
        print(f"\nCongratulations! Word was: {secret_word}")
        return score + 1
    else:
        return play_round(
            secret_word, guessed_letters, lives, score, start_time, time_limit, mode
        )


def main_menu(total_score=0):
    print("\n--- GUESS THE WORD: PRO EDITION ---")

    # Selection: Mode (New!)
    print("Modes: 1 (Play Yourself), 2 (Autoplay)")
    mode_input = input("Select mode: ")
    game_mode = CHOICES.get(mode_input, "You")

    # Selection: Category
    print(f"Categories: {', '.join(CATEGORIES.keys())}")
    cat_choice = input("Pick a category: ").title()
    global category_name
    category_name = cat_choice if cat_choice in CATEGORIES else "Food"

    # Selection: Difficulty
    print("Difficulties: 1 (Easy), 2 (Hard)")
    diff_choice = input("Select difficulty: ")
    settings = DIFFICULTY.get(diff_choice, DIFFICULTY["1"])

    word = random.choice(CATEGORIES[category_name])

    new_score = play_round(
        word,
        [],
        settings["lives"],
        total_score,
        time.time(),
        settings["timer"],
        game_mode,
    )

    print(f"--- TOTAL SCORE: {new_score} ---")

    if input("\nPlay another round? (y/n): ").lower() == "y":
        main_menu(new_score)
    else:
        print(f"Final Score: {new_score}. Goodbye!")


if __name__ == "__main__":
    main_menu()
