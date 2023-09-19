from lib.sentence_check import *

def test_full_stop():
    result = sentence_check('I was shopping.')
    assert result == True

def test_question():
    result = sentence_check('I was shopping.')
    assert result == True

def test_exclaim():
    result = sentence_check('I was shopping!')
    assert result == True

def test_no_punctuation():
    result = sentence_check('I was shopping')
    assert result == False

def test_empty():
    result = sentence_check("")
    assert result == False