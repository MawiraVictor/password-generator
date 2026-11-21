import secrets
import string
from typing import Dict


class PasswordGenerator:
    """Generate strong passwords using the cryptographically secure `secrets`
    module. `random` is NOT used anywhere here: it is seeded from the system
    clock and is predictable, which makes it unsafe for anything security
    related. `secrets` draws from the operating system's CSPRNG instead.
    """

    LOWER = string.ascii_lowercase
    UPPER = string.ascii_uppercase
    DIGITS = string.digits
    SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/"

    def generate(
        self,
        length: int = 16,
        use_upper: bool = True,
        use_lower: bool = True,
        use_digits: bool = True,
        use_symbols: bool = True,
    ) -> str:
        """Return a random password of `length` characters.

        The result is guaranteed to contain at least one character from every
        enabled set, so a generated password never accidentally drops a whole
        character class.
        """
        pools = []
        if use_lower:
            pools.append(self.LOWER)
        if use_upper:
            pools.append(self.UPPER)
        if use_digits:
            pools.append(self.DIGITS)
        if use_symbols:
            pools.append(self.SYMBOLS)

        if not pools:
            raise ValueError("Select at least one character set.")
        if length < len(pools):
            raise ValueError(
                f"Length must be at least {len(pools)} to include every selected set."
            )

        # One guaranteed character from each enabled pool...
        chars = [secrets.choice(pool) for pool in pools]
        # ...then fill the rest from the combined alphabet.
        alphabet = "".join(pools)
        chars += [secrets.choice(alphabet) for _ in range(length - len(chars))]

        # Shuffle so the guaranteed characters are not all at the front.
        secrets.SystemRandom().shuffle(chars)
        return "".join(chars)

    def generate_passphrase(self, words: int = 4, separator: str = "-") -> Dict:
        """Return a simple word-count passphrase placeholder note.

        A full passphrase needs a wordlist (e.g. EFF diceware); this reports
        what would be needed rather than shipping a fake one.
        """
        return {
            "supported": False,
            "note": (
                f"Passphrase generation needs a wordlist to pick {words} words from. "
                "Add an EFF diceware list to enable this."
            ),
            "separator": separator,
        }
