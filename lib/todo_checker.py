#As a user
#I want to check if a text includes the string #TODO
#So that I can keep track of my tasks

def todo_checker(text):
    count = 0
    split_text = text.split()
    for i in split_text:
        if i == '#TODO':
            count += 1
    return f"{count} tasks left."

