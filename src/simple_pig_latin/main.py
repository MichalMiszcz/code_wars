import re
import string


def pig_it(text):
    words = text.split()

    words_list = []
    for word in words:
        match = re.match(r'^.', word)

        if match:
            if match.group(0) in string.punctuation:
                words_list.append(word)
            else:
                final_word = word[match.end():] + match.group(0) + 'ay'
                words_list.append(final_word)

    final_sentence = ' '.join(words_list)
    return final_sentence

if __name__ == "__main__":
    print(pig_it("hello world"))
    print(pig_it("Pig latin is cool"))
    print(pig_it("O tempora o mores !"))