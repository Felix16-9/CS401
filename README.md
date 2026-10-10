# Crossword Word Guessing Game (CS401)

Team: Felix Nguyen, Jose Castillo

Startup prototype: a console grid with two hidden 5-letter words. Type a full word; if it matches, that row is revealed.

Words come from `words.db`, a SQLite database of exactly 50 five-letter words. Each game picks 2 of them at random.

## Run

```bash
python init_db.py
python game.py
```

`init_db.py` rebuilds the database. `game.py` creates it automatically if `words.db` is missing.
