def first_non_repeating_letter(s):
    lower_s = s.lower()
    for char in s:
        count = lower_s.count(char.lower())
        if count == 1:
            return char

    return ""



if __name__ == "__main__":
    print(first_non_repeating_letter("sTreSs"))
    print(first_non_repeating_letter("aaBBss"))
    print(first_non_repeating_letter("@#@@*"))
    print(first_non_repeating_letter("🐐🦊🐐"))