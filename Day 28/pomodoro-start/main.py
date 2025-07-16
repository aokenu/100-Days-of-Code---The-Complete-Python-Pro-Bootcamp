from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
BLUE = "#3D74B6"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # stop the timer
    window.after_cancel(timer)
    check_mark.config(text=" ")
    # change the title to "timer"
    timer_label.config(text="Timer", fg=GREEN)
    # reset the counter to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=BLUE)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Break", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        # countdown finished, increment reps and start again
        start_timer()
        marks=""
        work_sessions = math.floor(reps/2) # two reps make one session
        for _ in range(work_sessions): # this will loop through the number of session calculated above
            marks += "✓"
        check_mark.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

#Create text
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=1)


#Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row=0)

start_button = Button(text="Start", fg=BLACK, bg=YELLOW, font=(FONT_NAME, 11, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", fg=BLACK, bg=YELLOW, font=(FONT_NAME, 11, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)

check_mark = Label(text=" ", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 13, "bold"))
check_mark.grid(column=2, row=4)





window.mainloop()