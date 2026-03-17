import datetime
import time

alarm_time = input("Set alarm time (HH:MM:SS): ")

print("Waiting for alarm...")

while True:

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:

        print("\n⏰ ALARM! Wake up!")

        for i in range(5):
            print("BEEP!")
            time.sleep(1)

        break

    time.sleep(1)