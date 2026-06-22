from logic_utils import check_guess
from app import parse_guess


# --- Baseline behavior (check_guess returns an (outcome, message) tuple) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: high/low hint messages were swapped ---

def test_too_low_hint_tells_player_to_go_higher():
    # A guess below the secret must direct the player UP.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_too_high_hint_tells_player_to_go_lower():
    # A guess above the secret must direct the player DOWN.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


# --- Bug 2: secret was stringified on even attempts, forcing a lexicographic compare ---

def test_comparison_is_numeric_not_lexicographic():
    # 8 < 50 numerically, but "8" > "50" lexicographically. The fixed code
    # compares numbers, so guessing 8 against 50 must be "Too Low".
    outcome, message = check_guess(8, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


# --- Bug 3: out-of-range guesses (e.g. -1) were accepted ---

def test_guess_below_range_is_rejected():
    ok, value, err = parse_guess("-1", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."


def test_guess_above_range_is_rejected():
    ok, value, err = parse_guess("200", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."


def test_in_range_guess_is_accepted():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None
