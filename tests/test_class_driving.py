from lib.class_driving import *

entry = DiaryEntry('Happy', 'My Contents')
def test_init():
    assert entry.title == 'Happy'
    assert entry.contents == 'My Contents'

def test_format():
    assert entry.format() == 'Happy: My Contents'

def test_three_words():
    assert entry.count_words() == 'There are 2 words.'

def test_words():
    assert entry.reading_time(200) == '0 minutes.'