from typing import List


def str_counter(word: str):
       hashmap = {}
       # word = List(word)
       for i in list(word):
              hashmap[i] = 1 + hashmap.get(i, 0)
       return hashmap

print(str_counter("countcc"))