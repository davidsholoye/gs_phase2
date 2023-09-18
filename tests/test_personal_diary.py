from lib.personal_diary import *

def less_than_five():
    result = make_snippet('nope')
    assert result == 'nope'

def exactly_five():
    result = make_snippet('happy')
    assert result == 'happy'

def more_than_five():
    result = make_snippet('empathetic')
    assert result == 'empat'