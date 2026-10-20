# Daily Meditation Reminder

A Python script that reminds you to meditate on what you can do today, at a time you choose.

## Features
- Asks for a daily reminder time in HH:MM format (for example 09:00)
- Validates the input and asks again if the time is invalid
- Prints "Meditate on what you can do today" every day at that time

## Requirements
- Python 3
- The `schedule` library

## Installation
```
py -m pip install -r requirements.txt
```
The `-r` option tells pip to read the list of libraries from `requirements.txt`.

## Usage
```
py meditation_reminder.py
```
On macOS or Linux, use `python3` instead of `py`.

Example:
```
What time should I remind you? (like 09:00) 18:24
```
At 18:24 the program prints:
```
Meditate on what you can do today
```
Keep the window open. The reminder only works while the script is running.

## What I practiced
- Handling bad input with try / except
- while loops and break
- Using a third-party library (schedule)

## Future ideas
- A different message each day
- Phone notifications

## License
MIT. See the LICENSE file.

Built while learning Python with CS50P.
