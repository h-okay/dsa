tests = [
    ("racecar", True),
    ("listen", False),
    ("elbow", False),
    ("schoolmaster", False),
    ("rotator", True),
    ("deified", True),
    ("civic", True),
    ("level", True),
]


def is_palindrome(word):
    return word == word[::-1]


if __name__ == "__main__":
    for word, expected in tests:
        assert is_palindrome(word) == expected
    print("OK")
