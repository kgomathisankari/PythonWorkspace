import calendar
import tkinter as tk

frame = tk.Tk()
year = tk.StringVar()


def action():
    root = tk.Tk()

    calendar_label = calendar.calendar()


info_label = tk.Label(frame, text= "Enter a year below to see the calendar for that year", fg= "red").grid(row= 0, column= 0)

year_label = tk.Label(frame, text= "Year").grid(row= 1, column= 0)
year_entry = tk.Entry(frame, textvariable=year).grid(row= 1, column= 1)

show_calendar_button = tk.Button(frame, text= "Show Calendar", command= action).grid(row= 2, column= 0)

frame.mainloop()
