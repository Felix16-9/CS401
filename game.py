# Crossword Word Guessing Game — startup
# Hidden 5-letter words are chosen from words.db (50 words).

import random
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("words.db")


def load_puzzle_words(count=2):
    if not DB_PATH.exists():
        from init_db import create_database

        create_database()

    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("SELECT word FROM words ORDER BY word").fetchall()

    words = [row[0] for row in rows]
    if len(words) != 50:
        raise SystemExit(f"The word database must contain exactly 50 words, found {len(words)}.")
    return random.sample(words, count)


def play(words):
    grid = [["_" for _ in range(5)] for _ in words]
    print("Guess the hidden 5-letter words.\n")
    while any("_" in row for row in grid):
        for row in grid:
            print("[" + "][".join(row) + "]")
        print()
        guess = input("Enter a 5-letter word: ").strip().upper()
        if guess in words and "_" in grid[words.index(guess)]:
            grid[words.index(guess)] = list(guess)
            print("Correct!\n")
        else:
            print("Not in the puzzle.\n")
    print("You completed the puzzle!")


if __name__ == "__main__":
    play(load_puzzle_words())
