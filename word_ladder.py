#!/bin/python3
from collections import deque
import copy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
   A function that creates a word ladder that links one word to another in the quickest possible way
    '''

    stack = []
    stack.append(start_word)
    
    que = deque()
    que.appendleft(stack)
    
    word_file = open(dictionary_file).readlines()
    words = []
    
    if start_word == end_word:
        return [start_word]

    for x in word_file:
        words.append(x.strip("\n"))
        
    while len(que) != 0:
        top = que.pop()
        for word in words:
            if _adjacent(word,top[-1]):
                stack_copy = copy.deepcopy(top)
                stack_copy.append(word)
                if word == end_word:
                    for i in range(1,len(stack_copy)-2):
                        if _adjacent(top[i-1],top[i+1]):
                            stack_copy.pop(i)
                    return (stack_copy)
                que.appendleft(stack_copy)
                words.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if ladder == []:
        return False
    
    for word1, word2 in zip(ladder, ladder[1:]):
        if not _adjacent(word1, word2):
            return False
    return True

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise
    '''
    if word1 == word2:
        return False
    
    if len(word1) == len(word2):
        char_diff = 0
        for x,y in zip(word1, word2):
            if x!= y:
                if char_diff:
                    return False
                char_diff +=1
        return True
    else:
        return False
