'''Write a function, which takes a non-negative integer (seconds)
as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures'''


def makeTimeReadable(seconds):
    time_format = ''
    if seconds >= 0 and seconds < 360000:
        mins, sec = divmod(seconds, 60)
        hour, mins = divmod(mins, 60)
        time_format = "{:02d}:{:02d}:{:02d}".format(hour, mins, sec)
        
    return time_format


if __name__ == '__main__':
    seconds = 330000
    print makeTimeReadable(seconds)
