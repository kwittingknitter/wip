"""Decompose Hangul syllables into their jamo (letter) sequences.

안녕하세요 -> ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ
"""

SYLLABLE_START = 0xAC00
SYLLABLE_END = 0xD7A3

INITIALS = [
    "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ",
    "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ",
]

MEDIALS = [
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
    "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ",
]

FINALS = [
    "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ",
    "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ",
    "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ",
]


def decompose_syllable(char):
    """Split a single Hangul syllable into its jamo. Non-syllables pass through unchanged."""
    code = ord(char)
    if not (SYLLABLE_START <= code <= SYLLABLE_END):
        return char

    offset = code - SYLLABLE_START
    initial = offset // (21 * 28)
    medial = (offset % (21 * 28)) // 28
    final = offset % 28

    jamo = INITIALS[initial] + MEDIALS[medial]
    if final:
        jamo += FINALS[final]
    return jamo


def to_jamo(text):
    """Convert a string of Hangul syllables into a flat jamo sequence."""
    return "".join(decompose_syllable(char) for char in text)
