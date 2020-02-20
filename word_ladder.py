#!/bin/python3
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    
    if start_word == end_word:
        return [start_word]
    
    stack = []
    stack.append(start_word)
    que = deque()
    que.append(stack)
    
    word_list = open(dictionary_file).readlines()
    
    words = []
    
    for word in word_list:
        words.append(word.strip("\n"))
    while len(que) > 0:
        que.pop()
        for word in words:
            if _adjacent(word, stack[0]):
                if word == end_word:
                    stack.append(word)
                    return stack
                copy = deepcopy(stack)
                copy.append(word)
                que.appendleft(copy)
                words.remove(word)
    return None
 
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if ladder == []:
        return False
    for word1, word2 in zip(ladder, ladder[1:]):
        if not _adjacent(word1,word2):
            return False
        return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1)==len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
    if count == 3:
        return True
    else:
        return False
            
