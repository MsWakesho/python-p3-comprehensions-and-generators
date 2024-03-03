#!/usr/bin/env python3

def return_evens(num_list):
  return [num for num in num_list if num % 2 == 0]
num_list = [0, 1, 3, 5, 7, 8, 9]
evens = (return_evens(num_list))
print(evens)


def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list ]

sentence_list = ["I like computers","I require coffee","Live long and prosper"]
sentences_with_exclamation = (make_exclamation(sentence_list))
print(sentences_with_exclamation)