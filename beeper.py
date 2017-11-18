import winsound


FREQUENCY = 440
DURATION = 1000


def win_beep(num_beeps):
    while num_beeps:
        winsound.Beep(FREQUENCY, DURATION)
        num_beeps -= 1
