
# the format of the stopwatch------------
def format_time(elapsed_time):
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    miliseconds = int((elapsed_time % 1) * 1000)

    return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:03d}"
