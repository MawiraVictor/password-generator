#!/usr/bin/env python3
# Import works whether run as `python src/main.py`, `python main.py` from
# inside src/, or `python -m src.main` from the repo root.
try:
    from strength_checker import PasswordStrengthChecker
    from generator import PasswordGenerator
except ImportError:
    from src.strength_checker import PasswordStrengthChecker
    from src.generator import PasswordGenerator


def check_password(checker):
    password = input("\nEnter a password to check: ").strip()
    if not password:
        print("Please enter a password.")
        return

    result = checker.check_strength(password)
    print(f"\nPassword: {'*' * len(password)}")
    print(f"Strength: {result['strength']} (Score: {result['score']}/10)")
    print("\nFeedback:")
    for item in result['feedback']:
        print(f"  {item}")


def generate_password(generator, checker):
    raw = input("\nPassword length (default 16): ").strip()
    try:
        length = int(raw) if raw else 16
    except ValueError:
        print("That is not a number.")
        return

    try:
        password = generator.generate(length=length)
    except ValueError as e:
        print(f"Could not generate: {e}")
        return

    result = checker.check_strength(password)
    print(f"\nGenerated password: {password}")
    print(f"Strength: {result['strength']} (Score: {result['score']}/10)")


def main():
    checker = PasswordStrengthChecker()
    generator = PasswordGenerator()

    print("Password Tools")
    print("=" * 30)

    menu = (
        "\nChoose an option:"
        "\n  1) Check a password's strength"
        "\n  2) Generate a strong password"
        "\n  q) Quit"
        "\n> "
    )

    while True:
        choice = input(menu).strip().lower()
        if choice in ('q', 'quit'):
            break
        elif choice == '1':
            check_password(checker)
        elif choice == '2':
            generate_password(generator, checker)
        else:
            print("Please choose 1, 2, or q.")


if __name__ == "__main__":
    main()
