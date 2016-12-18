# Decode and save coded_message using caesar and key = -3. coded_message is already loaded from the previous problem.
# Store your decoded message as decoded_message.
# Print decoded_message. Does this recover your original message?

from Week3_CaseStudiesPart1.Case1_DNATranslation.Exercise.ex3 import caesar, coded_message

decoded_message = caesar(coded_message, key=-3)
print(decoded_message)