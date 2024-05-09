import tkinter as tk
from datetime import date


def calculate_age():
    today = date.today()
    birth_day = int(day_entry.get())
    birth_month = int(month_entry.get())
    birth_year = int(year_entry.get())

    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    result_label.config(text=f"Your age is: {age}")


# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.configure(bg='lightblue')  # Set background color

# Create a frame for group members
group_frame = tk.Frame(root, bg='lightblue')
group_frame.pack()

# Group members label
group_label = tk.Label(group_frame, text="Group Members: Alice, Bob, Charlie", bg='lightblue')
group_label.pack()

# Create labels for day, month, year
day_label = tk.Label(root, text="Day:", bg='lightblue')
day_label.place(x=50, y=50)

month_label = tk.Label(root, text="Month:", bg='lightblue')
month_label.place(x=50, y=80)

year_label = tk.Label(root, text="Year:", bg='lightblue')
year_label.place(x=50, y=110)

# Create entry fields for day, month, year
day_entry = tk.Entry(root)
day_entry.place(x=100, y=50)

month_entry = tk.Entry(root)
month_entry.place(x=100, y=80)

year_entry = tk.Entry(root)
year_entry.place(x=100, y=110)

# Create button
button = tk.Button(root, text="Calculate Age", command=calculate_age)
button.place(x=50, y=140)

# Create result label
result_label = tk.Label(root, text="", bg='lightblue')
result_label.place(x=50, y=170)

# Run the main loop
root.mainloop()
