from lib.personal_diary import *

def test_less_than_five():
    result = make_snippet('nope')
    assert result == 'nope'

def test_exactly_five():
    result = make_snippet('happy')
    assert result == 'happy'

def test_more_than_five():
    result = make_snippet('empathetic')
    assert result == 'empat'

def test_ten_words():
    result = count_words("Will you get a headache if you think too hard?")
    assert result == 10

def test_no_words():
    result = count_words('')
    assert result == 0