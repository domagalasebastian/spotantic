from collections.abc import Sequence

from pydantic import SecretStr


def sequence_to_str(seq: Sequence[str], separator: str) -> str:
    """Join a sequence of strings into a single string using the specified separator.

    Args:
        seq: Sequence of strings to join.
        separator: String to use as the separator.

    Returns:
        A single string with all items joined by `separator`.
    """
    return separator.join(seq)


def sequence_to_comma_separated_str(seq: Sequence[str]) -> str:
    """Join a sequence of strings into a single comma-separated string.

    Args:
        seq: Sequence of strings to join.

    Returns:
        A single string with all items separated by commas.
    """
    return sequence_to_str(seq=seq, separator=",")


def secret_str_to_str(secret_str: SecretStr) -> str:
    """Returns unmasked value of the ``SecretStr`` object.

    Args:
        secret_str: Secret string.

    Returns:
        The same string in the plain-text form.
    """
    return secret_str.get_secret_value()
