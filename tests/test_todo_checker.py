from lib.todo_checker import *

def test_empty_string():
    result = todo_checker("")
    assert result == "0 tasks left."

def test_one_task():
    result = todo_checker("#TODO : Make some breakfast. This is going to be eggs and bacon")
    assert result == "1 tasks left."

def test_five_tasks():
    result = todo_checker("#TODO : Make some breakfast. This is going to be eggs and bacon #TODO : Make some breakfast. This is going to be eggs and bacon #TODO : Make some breakfast. This is going to be eggs and bacon #TODO : Make some breakfast. This is going to be eggs and bacon #TODO : Make some breakfast. This is going to be eggs and bacon")
    assert result == "5 tasks left."