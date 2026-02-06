## ⏰ Dynamic Clock & Multi-Threaded Alarm

An interactive desktop application built with Python. This tool functions as both a visually adaptive clock and a reliable alarm system that plays audio notifications.

## ✨ Key Features

- Dynamic UI: The clock background changes colors (Blue, Yellow, Coral) and updates its greeting based on the time of day.
- Precision Alarm: Set hours, minutes, and seconds using a user-friendly dropdown menu.
- Multi-Threaded Performance: Uses Python's threading library so the alarm can run in the background without making the app unresponsive.
- Audio Alerts: Integrated with pygame.mixer to play high-quality .wav alarm sounds.

## 🛠️ Technical Stack

- GUI: tkinter
- Audio: pygame
- Threading: threading (to handle background time checks)
- Time Management: datetime and time

## 🚀 Setup & Installation

1. Install Dependencies
You will need the pygame library to handle the audio playback:
2. Make sure you are using **Python 3.10 – 3.12** (pygame is not compatible with newer versions yet).
3. Install the required dependency:
   
   ```bash
   pip install pygame

## 📖 How to Use

- iew Time: The main interface displays the current time and a contextual greeting.
- Set Alarm: Use the dropdown menus (OptionMenu) to select your desired wake-up time.
- Activate: Click "Set Alarm". The app will start a background thread to monitor the time.
- Silence: When the alarm triggers, click the "Stop Alarm" button to end the audio.

## 🧠 Code Logic Overview

The alarm system avoids "Application Not Responding" errors by offloading the while True loop to a separate thread:

Python

def Threading():
    t1 = Thread(target=alarm) # Create background process
    t1.start()

def alarm():
    while True:
        # Constantly checks if current_time == set_alarm_time
        ...

## 👤 Author

RaiTech Building tools that keep you on schedule.


