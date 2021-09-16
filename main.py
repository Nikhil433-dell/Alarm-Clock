# for making window
from tkinter import *


import time
from playsound import playsound
import datetime
from tkinter import messagebox

# creating root object
root = Tk()

# defining size of window
root.geometry("700x500")
root.title("Alarm Clock")


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    clock_label.config(text=f"{hour}:{minute}:{second}")
    clock_label.after(1000, clock)

frame = Frame(root, width=500)
frame.pack(side=TOP)

hour = time.strftime("%H")
minute = time.strftime("%M")
second = time.strftime("%S")
month_date = time.strftime("%d")
month = time.strftime("%B")
year = time.strftime("%Y")
day = time.strftime("%A")

clock_label = Label(frame,text=f"{hour}:{minute}:{second}" , font=( 'monospace',20 ))
clock_label.after(1000,clock)
clock_label.grid(row=0, column=1, pady=10)

clock_time = Label(frame, text=f"{day}\n {month_date} {month} , {year}")
clock_time.grid(row=2, column=1, pady=5)


# Alarm set

    

hor = IntVar()
min = IntVar()
sec = IntVar()

hor.set("")
min.set("")
sec.set("")



def set_alarm():
    hours = hor.get()
    minutes = min.get()
    seconds = sec.get()

    
    while (1 == 1):
        if (hours == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute and seconds == datetime.datetime.now().second ):
            playsound("clock_sound.mp3")
            break


    

    hor.set("")
    min.set("")
    sec.set("")

head = Label(frame, text="For Alarm Set", font=( 'system-ui', 20 ))
head.grid(row=3, column=1, pady=70)


hr_label = Label(frame, text="Hour", font=(12))
hr_label.grid(row=4, column=0, padx=4)

mn_label = Label(frame, text="Minute", font=(12))
mn_label.grid(row=5, column=0, padx=4)

sc_label = Label(frame, text="Second", font=(12))
sc_label.grid(row=6, column=0, padx=4)

hr = Entry(frame, textvariable=hor, borderwidth=2, width=30, relief=SOLID)
hr.grid(row=4, column=1, pady=10)

mn = Entry(frame, textvariable=min, borderwidth=2, width=30, relief=SOLID)
mn.grid(row=5, column=1, pady=5)

sc = Entry(frame, textvariable=sec, borderwidth=2, width=30, relief=SOLID)
sc.grid(row=6, column=1, pady=5)

alarm = Button(frame,text="Set Alarm", borderwidth=3, command=set_alarm , width=9)
alarm.grid(row=7, column=1, pady=5)



root.mainloop()