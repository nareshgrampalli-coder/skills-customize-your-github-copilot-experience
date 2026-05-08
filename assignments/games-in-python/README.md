# 📘 Assignment: Games in Python

## 🎯 Objective

In this assignment, you will build a simple Hangman game in Python. You will practice using strings, loops, conditionals, and user input to create an interactive game experience.

## 📝 Tasks

### 🛠️ Build the Game Setup

#### Description
Create the starting structure of your Hangman game. Prepare a list of possible words, randomly choose one word, and initialize the game state.

#### Requirements
Completed program should:

- Store at least five possible words in a list.
- Randomly choose one word from the list at the start of the game.
- Create a display version of the word using underscores for unguessed letters (for example: `_ _ _ _`).
- Set a fixed number of incorrect guesses allowed (for example: 6).

### 🛠️ Implement the Gameplay Loop

#### Description
Build the main game loop that accepts letter guesses, updates progress, and ends with a clear win or lose message.

#### Requirements
Completed program should:

- Ask the player to enter one letter each turn.
- Reveal correct letters in all matching positions of the hidden word.
- Decrease remaining attempts only when the guess is incorrect.
- End the game when the player guesses the full word or runs out of attempts.
- Display a clear final message for both win and lose outcomes.
