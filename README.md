# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

This project is a Streamlit number-guessing game where the player tries to find a randomly chosen secret number within a limited number of attempts, getting "higher/lower" hints and a running score along the way. While investigating, I found three bugs: (1) the hint messages were reversed, so a guess below the secret told the player to "Go LOWER" and a guess above it said "Go HIGHER"; (2) on even-numbered attempts the secret was converted to a string before comparison, which forced a lexicographic (text) comparison instead of a numeric one and produced wrong hints; and (3) input validation was missing, so out-of-range values like `-1` were accepted even though the UI states guesses must be between 1 and 100. To fix them, I swapped the hint messages back so the direction matches the comparison, removed the string conversion so the secret is always compared as an integer, and added a range check in `parse_guess` that rejects anything outside 1–100. I also refactored the core logic (`get_range_for_difficulty`, `parse_guess`, and `check_guess`) out of `app.py` into `logic_utils.py` and added pytest cases covering each fixed bug, all of which now pass.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of a number between 1-100, such as 40
2. Game returns "Too Low" or "Too high" based on secret number
3. User enters a follow-up guess
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= 9 passed in 0.01s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
