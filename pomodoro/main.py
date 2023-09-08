from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK="✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

#Screen setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=25,background=YELLOW)

#Label
name = Label(text="Timer",fg=GREEN,bg=YELLOW,highlightthickness=0, padx=15,pady=15,font=(FONT_NAME,40,"bold"))
name.grid(row=0,column=1)

#Image setup
canvas = Canvas(width=205,height=225,background=YELLOW, highlightthickness=0)
tomat_img = PhotoImage(file="Day28/pomodoro/tomato.png")
canvas.create_image(105,112, image=tomat_img)

#Timer
canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(row=1,column=1)

#Buttons
button_start = Button(text="Start",bg=YELLOW,highlightthickness=0)
button_start.grid(row=2,column=0)
button_reset = Button(text="Reset",bg=YELLOW, highlightthickness=0)
button_reset.grid(row=2,column=2)

#Ticks
tick = Label(text=CHECK_MARK,bg=YELLOW,highlightthickness=0,fg=GREEN,font=(FONT_NAME,20,"bold"),pady=15)
tick.grid(row=2,column=1)

window.mainloop()