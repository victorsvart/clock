from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Clock")
app_window.geometry("375x150")
app_window.resizable(1, 1)

text_font = ("Segoe UI", 68, "italic")
background = "#30a2c4"
foreground = "#000000"
border_width = 20

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, clock)


clock()
app_window.mainloop()
