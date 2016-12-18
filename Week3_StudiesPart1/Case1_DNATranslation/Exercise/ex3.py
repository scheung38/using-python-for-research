# Create a function caesar(message, key) that includes coded_message to encode a message
# with the caesar cipher. alphabet and letters are preloaded from the previous exercise.
# Use caesar to encode message using key = 3, and save the result as coded_message.
# Print coded_message.


from Week3_StudiesPart1.Case1_DNATranslation.Exercise.ex2 import alphabet, letters, coded_message

key = 3


def caesar(message, key):
    """
    :param message: message is the input dictionary
    :param key: key is the number of shifts
    :return: return the encoded message as a single string!
    """
    coded_message_string = "".join([letters[coded_message[letter]] for letter in message])

    return coded_message_string


coded_message = caesar(message, key=3)
print(coded_message)
