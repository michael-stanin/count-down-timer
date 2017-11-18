import sys
import time
from beeper import win_beep


NUM_BEEPS = 5


def count_down_timer(minutes):
    t = minutes * 60
    while t:
        mins, secs = divmod(t, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t-=1
    print("Done.")
    win_beep(NUM_BEEPS)


if __name__ == "__main__":
    count_down_timer(int(sys.argv[1]))