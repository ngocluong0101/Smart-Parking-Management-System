import re


def normalize_plate(raw: str) -> str:
    """
    Normalize license plate text: uppercase, remove non-alphanumeric except dash,
    collapse spaces, and perform simple replacements for common OCR confusions.

    Examples:
    - "29a-12345" -> "29A-12345"
    - "  29 a 12345 " -> "29A12345"

    This is intentionally conservative; adjust rules for local plate formats.
    """
    if not raw:
        return ""

    s = raw.strip().upper()

    # common OCR corrections
    replacements = {
        'O': '0',  # letter O to zero
        'I': '1',  # letter I to one
        'Z': '2',  # sometimes Z<->2
        'S': '5',  # S <->5 confusion
    }

    # Remove characters not alnum or dash
    s = re.sub(r"[^A-Z0-9\- ]+", "", s)
    s = s.replace(' ', '')

    # Replace obvious char confusions but be conservative: only replace when pattern suggests
    # For simplicity apply replacements across string where they make sense (digits expected)
    normalized_chars = []
    for ch in s:
        if ch in replacements:
            normalized_chars.append(replacements[ch])
        else:
            normalized_chars.append(ch)

    s = ''.join(normalized_chars)

    # Remove leading/trailing dashes
    s = s.strip('-')

    # Final sanity: keep only alnum and dash
    s = re.sub(r"[^A-Z0-9\-]", "", s)

    return s


def is_valid_plate(plate: str) -> bool:
    """
    Basic validation of normalized plate. This should be adapted per country rules.
    Here: require at least 4 characters and at most 12, and must contain digits.
    """
    if not plate:
        return False
    if len(plate) < 4 or len(plate) > 12:
        return False
    if not re.search(r"\d", plate):
        return False
    return True
