# Create a function word_count_distribution(text) that takes a book string and outputs a dictionary with items corresponding to the count of times a collection of words appears in the translation, and values corresponding to the number of number of words that appear with that frequency. Can you accomplish this by using count_words_fast(text) in your function?
# "Romeo and Juliet" is preloaded as text. Call word_count_distribution(text), and save the result as distribution.

from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Week3_StudiesPart1.Case2_Introduction_to_LanguageProcessing.counting_words.counting_words import \
    count_words_fast

text = "There is some txt from Shakespeare"


# Ex1
def word_count_distribution(text):
    word_counts = count_words_fast(text)
    count_distribution = Counter(word_counts.values())
    return count_distribution


distribution = word_count_distribution(text)


# Ex2
def more_frequent(distribution):
    counts = sorted(distribution.keys())
    sorted_frequencies = sorted(distribution.values(), reverse=True)
    cumulative_frequencies = np.cumsum(sorted_frequencies)
    more_frequent = 1 - cumulative_frequencies / cumulative_frequencies[-1]
    return dict(zip(counts, more_frequent))


more_frequent(distribution)

# Ex3
hamlets = pd.DataFrame(columns=("language", "distribution"))
book_dir = "Books"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath + "Books/" + language + "/" + author + "/" + title + ".txt"
                text = read_book(inputfile)
                distribution = word_count_distribution(text)
                hamlets.loc[title_num] = language, distribution
                title_num += 1

# Ex4
colors = ["crimson", "forestgreen", "blueviolet"]
handles, hamlet_languages = [], []
for index in range(hamlets.shape[0]):
    language, distribution = hamlets.language[index + 1], hamlets.distribution[index + 1]
    dist = more_frequent(distribution)
    plot, = plt.loglog(sorted(list(dist.keys())), sorted(list(dist.values()),
                                                         reverse=True), color=colors[index], linewidth=2)
    handles.append(plot)
    hamlet_languages.append(language)
plt.title("Word Frequencies in Hamlet Translations")
xlim = [0, 2e3]
xlabel = "Frequency of Word $W$"
ylabel = "Fraction of Words\nWith Greater Frequency than $W$"
plt.xlim(xlim)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.legend(handles, hamlet_languages, loc="upper right", numpoints=1)
plt.show()
