def spin_words(sentence):
    words = sentence.split()

    final_list = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1]

        final_list.append(word)

    final_sentence = " ".join(final_list)
    return final_sentence

if __name__ == '__main__':
    sentence = "Stop spinning my words"
    final_sentence = spin_words(sentence)
    print(final_sentence)