# 📘 Assignment: Python Hangman Game

## 🎯 Objective

In this assignment, you will build a playable Hangman game using core Python concepts. You will practice working with strings, loops, conditionals, and user input while creating a fun console-based project.

## 📝 Tasks

### 🛠️	Set Up Core Game Logic

#### Description
Create the main game flow for Hangman. Choose a hidden word, keep track of guessed letters, and repeatedly ask the player for guesses until the game ends.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Display the word progress using underscores for unknown letters (for example: `_ _ _ _`).
- Ask the player to enter one letter per turn.
- Reveal correctly guessed letters in all matching positions.
- Reduce remaining attempts only when the guessed letter is not in the word.


### 🛠️	Finish Gameplay and End Conditions

#### Description
Improve the player experience by handling win and lose outcomes clearly. Make sure the game gives helpful feedback after each guess and ends correctly.

#### Requirements
Completed program should:

- Show the number of incorrect guesses remaining after each turn.
- Prevent duplicate guesses from counting as new incorrect attempts.
- End the game with a congratulatory message when the full word is guessed.
- End the game with a clear game-over message and reveal the word when attempts reach zero.
- Keep output readable and student-friendly with clear prompts and status updates.
