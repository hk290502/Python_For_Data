great_quotes = (
    "And we danced, on the brink of an unknown future, to an echo from a vanished past. (John Wyndham) \n" + \
    "Life is what happens to you while you're busy making other plans. (wrongly attributed to John Lennon)\n" + \
    "You cannot overestimate the unimportance of practically everything. (John Maxwell)"
)

def get_words(text):
    return text.split()


def count_words(words):
    return len(words)


def longest_word(words):
    return max(words, key=len).upper()

words = get_words(great_quotes)
print(words)
print(count_words(words))
print(longest_word(words))