
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game that uses random selection, strings, loops, conditionals, and user input. Players will guess letters to reveal a hidden word before they run out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word from the provided word list and initialize the variables needed to track the player's guesses and remaining attempts.

#### Requirements
Completed program should:

- Randomly select one word from the predefined `words` list.
- Track the letters the player has guessed.
- Set and track a maximum number of incorrect guesses.
- Display the hidden word as underscores, with spaces between letters.

### 🛠️ Run the Guessing Game

#### Description
Create a loop that asks the player for letter guesses, updates the displayed progress, and ends when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Ask the player to enter a letter and compare it with the secret word.
- Reveal correctly guessed letters in their positions in the word.
- Decrease the remaining attempts for each incorrect guess and show the updated count.
- End when the player has guessed the word or has no attempts remaining.
- Display a win message when the word is guessed and a loss message with the secret word when attempts run out.
