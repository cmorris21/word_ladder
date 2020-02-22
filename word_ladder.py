#!/bin/python3
from collections import deque
from copy import deepcopy
'''
Create a stack
Push the start word onto the stack
Create a queue
Enqueue the stack onto the queue

While the queue is not empty
    Dequeue a stack from the queue
    For each word in the dictionary
        If the word is adjacent to the top of the stack
            If this word is the end word
                You are done!
                The front stack plus this word is your word ladder.
            Make a copy of the stack
            Push the found word onto the copy
            Enqueue the copy
            Delete word from the dictionary
'''

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    
    if start_word == end_word:
        return [start_word]
        
    stack = []
    stack.append(start_word)
    que = deque()
    que.append(stack)
   
    word_file = open(dictionary_file).readlines()
    words = []

    for x in word_file:
        words.appendleft(x.strip("\n"))
    while len(que) != 0:
        top = que.pop()
        for word in words:
            remove = []
            if _adjacent(word,top[-1]): 
                copylist = copy.deepcopy(top)
                copylist.append(word)
                if word == end_word:
                    for i in range(1,len(copylist)-2):
                        if _adjacent(top[i-1],top[i+1]):
                            copylist.pop(i)
                    return (copylist)
                ourQ.appendleft(copylist)
                words.remove(word)
 
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
    for word1,word2 in zip(ladder, ladder[1:]):
        if not _adjacent(word1, word2):
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
    if word1 == word2:
        return False
    if len(word1)==len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
    if count == 3:
        return True
    else:
        return False
      
            
