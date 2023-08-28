from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
PINK2 = '#FFF0F5'
PINK3 = '#FBA1B7'
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 0.4

work_hours = 0
check_list =[]


def count_down(count):
    global work_hours
    if work_hours == 0:
        count = 0
        pass
    count_min = math.floor(count / 60)
    count_sec = math.ceil((count % 60))
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
    elif count == 0 and work_hours > 0:
        start()


def start():
    global work_hours
    work_hours += 1
    check_mark = ""
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    work_sec = WORK_MIN*60
    if work_hours % 2 == 0:
        check_list.append("✔️")
    for i in check_list:
        check_mark += i
    check.config(text=check_mark)

    if work_hours < 8 and work_hours % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break)
    elif work_hours > 8 and work_hours % 2 == 0:
        count_down(long_break)
        timer.config(text="Break", fg=RED)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


def reset():
    global work_hours
    check_list.clear()
    check.config(text="")
    timer.config(text="Timer", fg=GREEN)
    work_hours = 0


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Label
timer = Label(text="Timer", font=("Times New Roman", 35, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)
timer.config(padx=10, pady=10)

button_start = Button(text="Start", command=start, bg=PINK2, fg=PINK3)
button_start.grid(column=0, row=3)


button_reset = Button(text="Reset", command=reset, bg=PINK2, fg=PINK3)
button_reset.grid(column=2, row=3)


#Label_check
check = Label(text="", font=("Times New Roman", 10, "bold"), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)
check.config(padx=10, pady=10)

window.mainloop()
