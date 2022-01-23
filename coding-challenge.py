"""
Write a function that takes a string as an argument and returns a list of all the words inflected by "-ing".
Your function should also exclude all the mono-syllabic words ending in "-ing" (e.g. bing, sing, sling, ...).
Although these words end in "-ing", the "-ing" is not an inflection affix.
Consider a Mono-syllabic word as a word that only contains a vowell.

Examples
ingExtractor("coming bringing Letting sing") ➞ ["coming", "bringing", "Letting"]

ingExtractor("going Ping, king sHrink dOing") ➞ ["going",, "dOing"]

ingExtractor("zing went ring, ding wing SINk") ➞ []
"""

TEXT = "coming bringing Letting sing going Ping, king sHrink dOing zing went ring, ding wing SINk"


def ing_extractor(text: str) -> list:
    """
    Extracts words inflected by "-ing" excluding mono-syllabic words.
    Args:
        words (str): string characters with words to analyse.
    Returns
        (list) list of words that match criteria
    """
    def is_valid(word):
        if len([v for v in word if v.lower() in 'aeiou']) > 1:
            return 'ing' in word
        return False

    words = []
    word = ''
    excluded = (',', '.', ' ')

    for character in text:
        if character in excluded:
            if word:
                if is_valid(word):
                    words.append(word)
                word = ''
        else:
            word += character
    if word and is_valid(word):
        words.append(word)

    print(words)


"""
A palindrome is a series of letters or numbers that reads equivocally backwards.
Write a recursive function that determines whether a given string is a palindrome or not.
"""


def is_palindrome(word: str) -> bool:
    """
    Check if the given word is a palindrome or not using recursive method.
    Empty string and one letter are considered as palindrome.
    Args:
        word (str): string character to be checked.
    Returns
        (bool): boolean based on the result
    """
    def reversion(word):
        if len(word) < 2:
            return word
        return reversion(word[1:]) + word[0]

    return word == reversion(word)


"""
Given a dictionary of words (of any length) and an input word,
find all the dictionary words contained inside the input word.
Example, dictionary : a, aa, aaa , Input word : aaabaa, exit should be: a, a, a, aa, aa, aaa, a, a, aa.
"""

GIVEN_DICT = set(['a', 'aa', 'aaa'])
WORD_TEXT = 'aaabaa'


def find_key_occurrences(given_dict: set, text: str) -> list:
    """
    Find all overlapped occurrences of each given_dict's key into text.
    Args
        given_dict (set): dictionary of words to search.
        text (str): string of character where to search given_dict's keys.
    Returns
        (list): list with founded occurrences of key words.
    """
    import re
    output = []
    for key in given_dict:
        if key in text:
            occurrences = len(re.findall(f"(?={key})", text))
            output.extend([key] * occurrences)
    print(output)


if __name__ == '__main__':

    print(f"Executing ing_extractor for [{TEXT}]:\n")
    ing_extractor(TEXT)

    word = input("\nCheck if it's a palindrome: ")
    print("YES!") if is_palindrome(word) else print("No")

    print(
        f"Finding occurrences of keys in a given dict {GIVEN_DICT} into the text '{WORD_TEXT}':\n")
    find_key_occurrences(GIVEN_DICT, WORD_TEXT)
