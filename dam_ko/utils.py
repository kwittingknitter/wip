from random import choice
from vocab import *


def get_proper_name():
    first = choice(proper_names_parts)
    second = choice(proper_names_parts - first)
    return first + second

def get_dsm_morpheme(subj):
    """
    If subj ends in consonant, return -i
    If it ends in a vowel, return -ga
    """
    return ""

def get_dom_morpheme(obj):
    """
    If obj ends in consonant, return -ul
    If it ends in a vowel, return -lul
    """
    return ""

def get_diff_topic_morpheme(topic):
    """
    If topic ends in consonant, return -nun
    If it ends in a vowel, return -un
    """
    return ""
