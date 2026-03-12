"""
Unit tests for the hangman word-guess game.
Tests the update_game_state function for correctness and edge cases.
"""

from main import update_game_state


def test_correct_guess():
    """Correct guess: letter added, lives unchanged, not won."""
    guessed, lives, won = update_game_state("apple", [], "a", 6)
    assert guessed == ["a"]
    assert lives == 6
    assert won == False


def test_incorrect_guess():
    """Incorrect guess: letter added, lives decremented, not won."""
    guessed, lives, won = update_game_state("apple", [], "z", 6)
    assert guessed == ["z"]
    assert lives == 5
    assert won == False


def test_winning_guess():
    """Final correct guess completes the word: is_won = True."""
    guessed, lives, won = update_game_state("apple", ["a", "p", "l", "e"], "p", 6)
    assert won == True
    assert lives == 6


def test_duplicate_guess():
    """Duplicate guess: letter not added again, lives unchanged."""
    guessed, lives, won = update_game_state("apple", ["a"], "a", 6)
    assert guessed == ["a"]  # Not added again
    assert lives == 6


def test_case_insensitivity():
    """Uppercase guess recognized in lowercase word."""
    guessed, lives, won = update_game_state("Apple", [], "A", 6)
    assert guessed == ["a"]
    assert lives == 6


def test_single_letter_word_win():
    """Single-letter word guessed correctly: immediate win."""
    guessed, lives, won = update_game_state("a", [], "a", 6)
    assert guessed == ["a"]
    assert won == True
    assert lives == 6


def test_no_lives_left():
    """Guess with lives=0: lives stays 0 or goes negative."""
    guessed, lives, won = update_game_state("apple", [], "z", 0)
    assert lives == -1  # Decremented
    assert won == False

def test_lives_left_tracking():
    """Ensure lives_left is correctly updated after wrong and right guesses."""
    # start with a known number of lives
    guessed, lives, won = update_game_state("apple", [], "z", 3)
    assert lives == 2  # wrong guess decremented
    # subsequent correct guess should not change lives
    guessed, lives, won = update_game_state("apple", guessed, "a", lives)
    assert lives == 2
    assert not won


def test_all_letters_pre_guessed():
    """All letters already guessed: immediate win."""
    guessed, lives, won = update_game_state("apple", ["a", "p", "l", "e"], "x", 6)
    # Even though 'x' is wrong, all letters for "apple" are already guessed
    assert won == True


def test_multiple_correct_guesses():
    """Multiple correct guesses accumulate without losing lives."""
    guessed, lives, won = update_game_state("apple", ["a"], "p", 6)
    guessed, lives, won = update_game_state("apple", guessed, "l", lives)
    guessed, lives, won = update_game_state("apple", guessed, "e", lives)
    assert guessed == ["a", "p", "l", "e"]
    assert lives == 6
    assert won == True


if __name__ == "__main__":
    # Run all tests
    test_correct_guess()
    test_incorrect_guess()
    test_winning_guess()
    test_duplicate_guess()
    test_case_insensitivity()
    test_single_letter_word_win()
    test_no_lives_left()
    test_all_letters_pre_guessed()
    test_multiple_correct_guesses()
    print("✓ All tests passed!")
