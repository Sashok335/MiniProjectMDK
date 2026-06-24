import pytest
from game import generate_number, check_guess, play_game


class TestGenerateNumber:
    def test_generate_number_in_range(self):
        for _ in range(100):
            num = generate_number(-100, 100)
            assert -100 <= num <= 100

    def test_generate_number_min_equals_max(self):
        num = generate_number(42, 42)
        assert num == 42


class TestCheckGuess:
    def test_guess_correct(self):
        assert check_guess(50, 50) == "correct"

    def test_guess_too_high(self):
        assert check_guess(50, 70) == "too high"

    def test_guess_too_low(self):
        assert check_guess(50, 30) == "too low"

    def test_guess_boundary_high(self):
        assert check_guess(-100, -99) == "too high"

    def test_guess_boundary_low(self):
        assert check_guess(-100, -101) == "too low"


class TestPlayGame:
    def test_play_game_first_guess_correct(self):
        inputs = ["50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 1
        assert any("поздравляем" in o.lower() for o in outputs)

    def test_play_game_multiple_attempts(self):
        inputs = ["10", "30", "50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 3

    def test_play_game_low_then_high(self):
        inputs = ["30", "70", "50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 3
        hints = " ".join(o.lower() for o in outputs)
        assert "слишком мало" in hints
        assert "слишком много" in hints

    def test_play_game_edge_negative(self):
        inputs = ["-100", "0", "50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 3

    def test_play_game_invalid_input_not_counted(self):
        inputs = ["abc", "50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 1

    def test_play_game_out_of_range_not_counted(self):
        inputs = ["200", "50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 1

    def test_play_game_empty_string_does_not_crash(self):
        inputs = ["", "50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 1

    def test_play_game_whitespace_string_does_not_crash(self):
        inputs = ["   ", "50"]
        outputs = []
        attempts = play_game(
            secret=50,
            min_val=-100,
            max_val=100,
            input_func=lambda: inputs.pop(0),
            output_func=lambda msg: outputs.append(msg),
        )
        assert attempts == 1
