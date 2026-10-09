# Crossword Word Guessing Game — startup
# Hidden 5-letter words; guess until the grid is complete.

WORDS = ["APPLE", "GRAPE"]
grid = [["_" for _ in range(5)] for _ in WORDS]

print("Guess the hidden 5-letter words.\n")
while any("_" in row for row in grid):
    for row in grid:
        print("[" + "][".join(row) + "]")
    print()
    guess = input("Enter a 5-letter word: ").strip().upper()
    if guess in WORDS and "_" in grid[WORDS.index(guess)]:
        grid[WORDS.index(guess)] = list(guess)
        print("Correct!\n")
    else:
        print("Not in the puzzle.\n")
print("You completed the puzzle!")
