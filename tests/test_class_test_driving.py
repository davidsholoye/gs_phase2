from lib.class_test_driving import *
entry = DiaryEntry('Happy', 'My Contents')

assert entry.title == 'Happy'
assert entry.contents == 'My Contents'

assert entry.format() == 'Happy: My Contents'