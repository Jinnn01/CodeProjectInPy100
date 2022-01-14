from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer",fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# once click start ,start the countdown
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = count // 60
    sec = count % 60
    if sec >= 10:
        sec = str(sec)
    else:
        sec = "0" + str(sec)
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    #   就结束了，无法触发starter time 开始计数
    else:
        start_timer()
        # complete session add checkmark
        if reps % 2 == 0:
            checkmark = "✔" * (reps // 2)
            checkmark_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# add img
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# set timer label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_label.grid(column=1, row=0)

# set start button
start_button = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start_button.grid(column=0, row=2)
# set reset button
reset_button = Button(text="Reset", highlightbackground=YELLOW,command=timer_reset)
reset_button.grid(column=2, row=2)

# checkmark
checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()
