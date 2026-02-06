import tkinter as tk
from time import strftime


# ---------------- MAIN WINDOW ----------------
top = tk.Tk()
top.title("Dynamic Clock (By RaiTech)")
top.resizable(False, False)


# ---------------- FUNCTIONS ----------------
def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    else:
        return "Evening"


def update_time():
    current_time = strftime("%H:%M:%S %p")
    hour = int(strftime("%H"))
    time_of_day = get_time_of_day(hour)

    # Update label text
    clock_time.config(
        text=f"{current_time}\nGood {time_of_day}!"
    )

    # Change background color based on time of day
    if time_of_day == "Morning":
        color = "lightblue"
    elif time_of_day == "Afternoon":
        color = "lightyellow"
    else:
        color = "lightcoral"

    top.configure(background=color)

    # Update every second
    clock_time.after(1000, update_time)


# ---------------- WIDGETS ----------------
clock_time = tk.Label(
    top,
    font=("Courier New", 49),
    background="white",
    foreground="black"
)

clock_time.pack(anchor="center")


# ---------------- START APP ----------------
update_time()
top.mainloop()
