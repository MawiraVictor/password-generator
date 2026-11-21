import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from strength_checker import PasswordStrengthChecker


def test_empty_password_is_weak():
    c = PasswordStrengthChecker()
    result = c.check_strength("")
    assert result["score"] == 0
    assert result["strength"] == "Weak"


def test_common_password_is_penalised():
    c = PasswordStrengthChecker()
    result = c.check_strength("password")
    # "password" is in the common list, which drives the score to the floor.
    assert result["score"] == 0


def test_strong_password_scores_high():
    c = PasswordStrengthChecker()
    result = c.check_strength("Zt7$kQ9!mB2#wL4x")
    assert result["score"] >= 6
    assert result["strength"] in ("Strong", "Very Strong")


def test_result_shape():
    c = PasswordStrengthChecker()
    result = c.check_strength("abc")
    assert set(["score", "strength", "feedback", "color"]).issubset(result.keys())
    assert isinstance(result["feedback"], list)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("all strength-checker tests passed")
