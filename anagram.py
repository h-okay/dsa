tests = [
    ("dormitory", "dirty room"),
    ("astronomer", "moon starer"),
    ("conversation", "voices rant on"),
    ("funeral", "real fun"),
    ("listen", "silent"),
    ("elbow", "below"),
    ("schoolmaster", "the classroom"),
    ("forty five", "over fifty"),
    ("pears", "spear"),
    ("Debit card", "bad credit"),
    ("yes", "no"),
    ("evil", "good"),
]


def is_anagram(word1: str, word2: str) -> bool:
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)


def main():
    for word1, word2 in tests:
        print(f"{word1} - {word2}:", is_anagram(word1, word2))


if __name__ == "__main__":
    main()
