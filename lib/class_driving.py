class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        contents = self.contents.split()
        contents_len = len(contents)
        return f"There are {contents_len} words."
        

    def reading_time(self, wpm):
        x = len(self.contents.split())
        time = x//wpm
        rounded_time= round(time, 1)
        return f"{rounded_time} minutes."
