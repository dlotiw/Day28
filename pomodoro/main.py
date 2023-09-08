from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK="✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_click():
    global rep
    global timer
    rep = 0
    window.after_cancel(timer)
    timer = None
    tick.config(text="")
    canvas.itemconfig(timer_text, text="25:00")

    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def add_check(str=""):
    n = str+CHECK_MARK
    return n



def timer_mechanism():
    global rep
    rep += 1
    if rep % 8 == 0:
        tick.config(text=add_check(tick.cget("text")))
        name.config(text="Long break")
        countdown(0,20)
    elif(rep %2 == 0):
        tick.config(text=add_check(tick.cget("text")))
        name.config(text="Short break")
        window.focus_set()
        countdown(0,10)
    else:
        name.config(text="Work")
        countdown(0,15)
    
           
    

def button_start_click():
    timer_mechanism()

       

        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(min,sec=0):
    global timer
    if(sec < 10):
        canvas.itemconfig(timer_text, text=f"{min}:0{sec}")
    elif(sec >= 10):
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if (sec==0 and min > 0):
        timer = window.after(1000,countdown,min-1,59)
    elif (sec>0):
        timer = window.after(1000,countdown,min,sec-1)
    else:
        timer_mechanism()
    



# ---------------------------- UI SETUP ------------------------------- #

#Screen setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=25,background=YELLOW)
window.minsize(650,300)

#Label
name = Label(text="Pomodoro",fg=GREEN,bg=YELLOW,highlightthickness=0, padx=15,pady=15,font=(FONT_NAME,40,"bold"),width=10)
name.grid(row=0,column=1)

#Image setup
canvas = Canvas(width=205,height=225,background=YELLOW, highlightthickness=0)
tomat_img = PhotoImage(file="Day28/pomodoro/tomato.png")
canvas.create_image(105,112, image=tomat_img)

#Timer
timer_text = canvas.create_text(103,130,text="25:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(row=1,column=1)

#Buttons
button_start = Button(text="Start",bg=YELLOW,highlightthickness=0,command=button_start_click)
button_start.grid(row=2,column=0)
button_reset = Button(text="Reset",bg=YELLOW, highlightthickness=0,command=reset_click)
button_reset.grid(row=2,column=2)

#Ticks
tick = Label(text="",bg=YELLOW,highlightthickness=0,fg=GREEN,font=(FONT_NAME,20,"bold"),pady=15)
tick.grid(row=2,column=1)

window.mainloop()