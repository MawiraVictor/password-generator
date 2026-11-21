import os
import sys
import inspect

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from generator import PasswordGenerator


def test_length_is_respected():
    g = PasswordGenerator()
    assert len(g.generate(12)) == 12
    assert len(g.generate(32)) == 32


def test_contains_every_selected_class():
    g = PasswordGenerator()
    p = g.generate(20)
    assert any(c.islower() for c in p)
    assert any(c.isupper() for c in p)
    assert any(c.isdigit() for c in p)
    assert any(c in g.SYMBOLS for c in p)


def test_outputs_are_distinct():
    g = PasswordGenerator()
    passwords = {g.generate(16) for _ in range(20)}
    # Collisions from a CSPRNG at this length are astronomically unlikely.
    assert len(passwords) == 20


def test_too_short_is_rejected():
    g = PasswordGenerator()
    try:
        g.generate(2)  # fewer chars than enabled sets
    except ValueError:
        return
    raise AssertionError("expected ValueError for too-short length")


def test_uses_secrets_not_random():
    src = inspect.getsource(PasswordGenerator)
    module_src = inspect.getsource(sys.modules[PasswordGenerator.__module__])
    assert "secrets" in module_src
    assert "import random" not in module_src


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("all generator tests passed")
