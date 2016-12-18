from collections import Counter

text = "This comprehension check is to check for comprehension."


def count_words(text):
    """
    :param text: input string
    :return: the frequency count of each word
    """
    word_count = {}
    text = text.lower()
    skips = [".", ",", ";", ":", '"']
    for ch in skips:
        text = text.replace(ch, "")

    words = text.split(" ")
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def count_words_fast(text):
    """
    :param string_input: input string
    :return: the frequency count of each word
    """
    text = text.lower()
    skips = [".", ",", ";", ":", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_count = Counter(text.split(" "))
    return word_count


if __name__ == '__main__':
    print(count_words(text))
    print(count_words(text) == count_words_fast(text))
# True


# What pandas method allows you to insert a row to a dataframe?
# loc

# How can you retrieve the first and last few rows of a pandas dataframe called stats ?
# stats.head() and stats.tail()

# stats is a Pandas dataframe as defined in Video 3.2.6. How can you access the column "length" in this dataframe?
# stats.length
# stats["length"]

# stats is a Pandas dataframe as defined in Video 3.2.6. How can you select only the rows where the language is French?
# stats[stats.language == "French"]
