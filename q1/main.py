from tkinter import *
from component import Component
def run_screen():
    tk = Tk()
    tk.title("Youtube like interface")
    tk.resizable(0,0)
    tk.wm_attributes('-topmost',1)
    canvas = Canvas(tk, width=800,height= 500, bd=0, highlightthickness=0)
    canvas.pack()
    component =Component(canvas)
    component.draw_text("Youtube", 70, 20,"red", ('Times', 30))
    #canvas.create_text(70,20, text = "Youtube",fill = "red", font=('Times',30))
    
    #drawing components on the screen
    component.draw_componet(10, 50,200, 450 )
    component.draw_componet(220, 50, 470, 200)
    component.draw_componet(480, 50, 730, 200)
    component.draw_componet(220, 220, 470, 420)
    component.draw_componet(480, 220, 730, 420)
    
    #drawing text on componets
    component.draw_text("Live",100,100,"black",('Times',25))
    component.draw_text("Subscriptions",100,150,"green",('Times',25))
    component.draw_text("Favorites",100,250,"black",('Times',25))
    
    #drawing serarch box
    
    component.draw_componet(150,10,730,40)
    component.draw_text("search",200, 20, fill= "black", font=('Times',15))
    
    # drawing polygon image on screen
    component.draw_button(220, 50, 470, 200)
    component.draw_button(480, 50, 730, 200)
    component.draw_button(220, 220, 470, 420)
    component.draw_button(480, 220, 730, 420)
    
    # text to display title of the song
    
    component.draw_text("Video description one",345, 175, fill ="black", font=('Times',20))
    component.draw_text("Video description two",605, 175, fill ="black", font=('Times',20))
    component.draw_text("Video description three",345, 405, fill ="black", font=('Times',20))
    component.draw_text("Video description four",605, 405, fill ="black", font=('Times',20))
    tk.update()
    
    while True:
        
        tk.update_idletasks()
        tk.update()

run_screen()