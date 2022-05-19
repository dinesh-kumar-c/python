

def read_file(filename):
    all_words = []
    with open(filename, "r") as fp:
        data = fp.readlines()
    for line in data:
        for word in line.split():
            all_words.append(word)
    return all_words


def word_freq(all_words):
    word_counter = {}
    for word in all_words:
        if word in word_counter.keys():
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    most_freq_words = []
    most_frequency = 0
    for word, freq in word_counter.items():
        if freq > most_frequency:
            most_freq_words = []
            most_freq_words.append(word)
            most_frequency = freq
        elif freq == most_frequency:
            most_freq_words.append(word)

    return most_frequency, most_freq_words


al_words = read_file("sampletext.txt")
print(word_freq(al_words))


from collections import Counter

count = Counter(al_words)
print(count.most_common())
