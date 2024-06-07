import sys
from utils.genericObjFactory import createBlankObj
from datetime import datetime


def prompForNameAndColor():
    """
    Prompts the user for their name and favorite color,
    """
    name = input("What is your name? ")
    color = input("What is your favorite color? ")
    result = createBlankObj()
    result.name = name
    result.color = color
    return result

# Assuming createBlankObj is defined or imported correctly elsewhere

def promptForAge():
    """
    Prompts the user for their birth year and calculates their age.
    """
    birth_year = input("What is your birth year? ")
    current_year = datetime.now().year
    return current_year - int(birth_year)