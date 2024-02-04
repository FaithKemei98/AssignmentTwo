from tkinter import *

def run_screen():
    tk = Tk()
    tk.title("Youtube like interface")
    tk.resizable(0,0)
    tk.wm_attributes('-topmost',1)
    canvas = Canvas(tk, width=500,height= 500, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    
    
    while True:
        tk.update_idletasks()
        tk.update()

run_screen()