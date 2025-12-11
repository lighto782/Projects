"""
A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
"""

import time
import simpleaudio as sa  # type: ignore[import-untyped]

alarm_sound = sa.WaveObject.from_wave_file("/home/me/Projects-1/My Sulotions/Numbers/AlarmClock/ranan_fixed.wav")

def Alarm(minutes: int):
    seconds = 60 * minutes
    start_time = int(time.time())
    end_time = start_time + seconds
    while True:
        time_now = int(time.time())
        if time_now == end_time:
            print("00:00:00.0")
            alarm_sound.play()
            time.sleep(10)
            return "\nDONE!"
        else:
            time.sleep(0.1)
            time_in = end_time - time.time()
            time_in, sec = divmod(time_in, 60)
            hours, min = divmod(time_in, 60)
            print(f"{hours:02.0f} : {min:02.0f} : {sec:04.1f}", end="\r")
    


mins = int(input("Enter the amount of time in minutes: "))

print(Alarm(mins))