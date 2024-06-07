import sys
from utils.genericObjFactory import createBlankObj


def prompForNameAndColor():
    name = input("What is your name? ")
    color = input("What is your favorite color? ")
    result = createBlankObj()
    result.name = name
    result.color = color
    return result