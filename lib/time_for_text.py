def time_for_text(text):
    x = len(text.split()) / 200
    xx = round(x ,1)
    return f"{xx} minutes"