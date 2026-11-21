## A small project exploring Python and password security

# Password Tools

A collection of password utilities:
- Password strength checker
- Password generator (cryptographically secure)

# Features
- Password strength analysis (weak → very strong)
- Common password detection (blocks well-known weak passwords)
- Pattern recognition (flags repeats and common sequences)
- Real-time feedback on what makes the password weak
- Secure password generation using Python's `secrets` module (never `random`),
  guaranteeing at least one character from every selected character set

# Usage
```bash
# from the repo root
python -m src.main
# or from inside src/
python main.py
```
Then choose **1** to check a password or **2** to generate one.

# Why `secrets` and not `random`?
`random` is seeded from predictable state and is not safe for security use.
`secrets` draws from the operating system's CSPRNG, so generated passwords
cannot be reproduced by guessing a seed.
