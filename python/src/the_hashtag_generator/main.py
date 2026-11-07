

def generate_hashtag(s):
    list_of_words = s.lower().split()
    if len(list_of_words) == 0:
        return False

    hashtag_sentence = '#'
    for word in list_of_words:
        hashtag_sentence += word.capitalize()

    print(len(hashtag_sentence))
    if len(hashtag_sentence) <= 140:
        return hashtag_sentence
    else:
        return False

if __name__ == '__main__':
    print(generate_hashtag('Codewars'))
    print(generate_hashtag('      Codewars'))
    print(generate_hashtag('      '))
    print(generate_hashtag('CoDeWaRs is niCe'))
    print(generate_hashtag('c i n'))
    print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
    print(generate_hashtag('ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqqq'))