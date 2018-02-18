# TEMPLATE: http://www.codeskulptor.org/#poc_wrangler_template.py
# TASK: https://www.coursera.org/learn/principles-of-computing-2/supplement/xl26r/mini-project-description
# OWLTEST: http://codeskulptor.appspot.com/owltest?urlTests=poc.poc_wrangler_tests.py&urlPylintConfig=poc.pylint_config_wrangler.py&imports=%7Bpoc:(poc_wrangler_provided)%7D
# IMPLEMENTATION: http://www.codeskulptor.org/#user43_hMg1FaUxPWLys45_9.py
# WORDFILE: http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt

"""
Student code for Word Wrangler game
"""

import urllib2
# import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if not len(list1):
        return []
    output = [list1[0]]
    for element in list1:
        if output[-1] != element:
            output.append(element)
    return output


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    output = list()
    for item in list1:
        if item in list2:
            output.append(item)
    return output


# Functions to perform merge sort


def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    output = list()
    substitute1 = list1[:]
    substitute2 = list2[:]
    while len(substitute1) and len(substitute2):
        if substitute1[0] <= substitute2[0]:
            new = substitute1.pop(0)
            output.append(new)
        else:
            new = substitute2.pop(0)
            output.append(new)
    if len(substitute1):
        output.extend(substitute1)
    elif len(substitute2):
        output.extend(substitute2)
    return output


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if not len(list1):
        return []
    substitute = list1[:]
    if len(substitute) == 0:
        return []
    first = [substitute.pop(0)]
    merged = merge(first, merge_sort(substitute))
    return merged


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if not len(word):
        return['']
    output = list()
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    for string in rest_strings:
        output.append(string)
        for idx in xrange(len(string) + 1):
            listed_string = list(string)
            listed_string.insert(idx, first)
            new_string = ''.join(listed_string)
            output.append(new_string)
    return output


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()


if __name__ == '__main__':
    # a = [1, 1, 1, 1, 1]
    # b = [1, 1, 1, 2]
    # c = [2, 6, 8, 8, 9, 14]
    # print remove_duplicates(a), 'EXPECTED: [1]'
    # print remove_duplicates(b), 'EXPECTED: [1, 2]'
    # print remove_duplicates(c), 'EXPECTED: [2, 6, 8, 9, 14]'
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    c = [1, 2, 3]
    d = [2, 3, 4, 5]
    e = [80, 90, 92, 93]
    f = [1, 2, 3, 4, 90, 91, 92, 95, 100]
    g = [1]
    h = [3, 5, 1, 3, 6, 2, 0, 100, 99]
    # print intersect(a, b), 'EXPECTED: [3, 4, 5]'
    # print intersect(c, d), 'EXPECTED: [2, 3]'
    # print intersect(f, e), 'EXPECTED: [90, 92]'
    # print merge([1, 2, 3], [1, 2, 3])
    print merge_sort(h)
    # print gen_all_strings('aab')