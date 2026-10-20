import schedule
import time

#the reminder
def say_remind():
    print("Meditate on what you can do today")

#ask for a valid time
while True:
    reminder_time = input("What time should I remind you? (like 09:00) ")
    try:
        schedule.every().day.at(reminder_time).do(say_remind)
        break
    except schedule.ScheduleValueError:
        print("That's not a valid time, use HH:MM like 09:00")

#what keeps it counting
while True:
    schedule.run_pending()
    time.sleep(1)
