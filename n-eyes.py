#!/usr/bin/env python3

from copy import deepcopy
from random import randrange, sample, choice

def base(a: dict, b: dict) -> dict:
    return dict(list(a.items()) + list(b.items()))

def merge(into: dict, source: dict):
    keys = set(into.keys()).union(source.keys())
    for k in keys:

        try:
            new = source[k]
        except KeyError:
            continue

        try:
            into[k] += new
        except KeyError:
            into[k] = new

def indef(x: str) -> str:
    return ("an " if x[0].lower() in 'aeiou' else "a ") + x

def suited(worn: str) -> str:
    return "in {} suit".format(indef(worn))

def prep_fn(prep: str):
    return lambda x: " ".join([prep, indef(x)])

snake = { "eyes": 2,
          "noses": 1,
          "filters": [suited, prep_fn("on"), prep_fn("with"), prep_fn("riding")]}

animal = base(snake, {"legs": 4})
insect = base(snake, {"legs": 6})
centipede = base(snake, {"legs": 100})
millipede = base(snake, {"legs": 1000})

human = base(snake, {"legs": 2, "filters": [suited, prep_fn("on"), prep_fn("with")]})

ridable = {"filters": [prep_fn("riding"), prep_fn("on")]}
bicycle = base(ridable, {"wheels": 2})
pogo_stick = base(ridable, {"legs": 1})

classes = {
    "snake": snake,
    "pogo stick": pogo_stick,
    "chicken": human,
    "old man": human,
    "guy": human,
    "goat": animal,
    "elephant": animal,
    "cat": animal,
    "dog": animal,
    "lizard": animal,
    "ant": insect,
    "butterfly": insect,
    "centipede": centipede,
    "millipede": millipede,

    "bike": bicycle,
    "bicycle": bicycle,
}

contributors = sample(classes.keys(), randrange(2, 6))
answer = " ".join([indef(contributors[0])] + [ choice(classes[k]["filters"])(k) for k in contributors[1:] ])

combined = {}
for d in contributors:
    merge(combined, classes[d])
del combined["filters"]

print("Q: What has", ", ".join([ "{} {}".format(v, k) for k, v in combined.items() ]) + "?")
print("A:", answer.capitalize() + ".")
