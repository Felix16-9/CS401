"""Create the crossword word database: exactly 50 five-letter words."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("words.db")

WORDS = [
    "APPLE", "GRAPE", "BREAD", "CHAIR", "PLANT",
    "HOUSE", "WATER", "LIGHT", "MUSIC", "SMILE",
    "STONE", "RIVER", "CLOUD", "TIGER", "HORSE",
    "MOUSE", "EAGLE", "SHARK", "LEMON", "MANGO",
    "PEACH", "MELON", "OLIVE", "ONION", "BEACH",
    "OCEAN", "STORM", "FLAME", "FROST", "BRAVE",
    "QUIET", "HAPPY", "LUCKY", "SWEET", "FRESH",
    "GREEN", "BLACK", "WHITE", "BROWN", "PAPER",
    "TABLE", "CLOCK", "TRAIN", "PLANE", "HEART",
    "DREAM", "NIGHT", "WORLD", "MAGIC", "QUEEN",
]


def create_database():
    if len(WORDS) != 50:
        raise ValueError(f"Expected 50 words, found {len(WORDS)}.")
    if len(set(WORDS)) != 50:
        raise ValueError("Word list contains duplicates.")
    for word in WORDS:
        if len(word) != 5 or not word.isalpha() or word != word.upper():
            raise ValueError(f"Invalid word: {word}")

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DROP TABLE IF EXISTS words")
        conn.execute(
            """
            CREATE TABLE words (
                id INTEGER PRIMARY KEY,
                word TEXT NOT NULL UNIQUE CHECK (length(word) = 5)
            )
            """
        )
        conn.executemany(
            "INSERT INTO words (word) VALUES (?)",
            [(word,) for word in WORDS],
        )
    return DB_PATH


if __name__ == "__main__":
    path = create_database()
    print(f"Created {path.name} with {len(WORDS)} five-letter words.")
