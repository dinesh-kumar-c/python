## May 2022

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

    # count the freq of all the words and put them into word_counter
    for word in all_words:
        if word in word_counter.keys():
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    most_freq_words = []
    most_frequency = 0

    # get the most frequent after reading the word_counter dictionary
    for word, freq in word_counter.items():
        if freq >= most_frequency:
            # if we find the most_freq word the most_freq_words list
            # is not valid anymore and must be reset
            most_freq_words = []

            most_freq_words.append(word)
            most_frequency = freq
        elif freq == most_frequency:
            # id the frequency is equal then add the word to our most freq list
            most_freq_words.append(word)

    return most_frequency, most_freq_words


al_words = read_file("sampletext.txt")
print(word_freq(al_words))

# verify if our logic correct by using the Counter collections
from collections import Counter

count = Counter(al_words)
print(count.most_common())
