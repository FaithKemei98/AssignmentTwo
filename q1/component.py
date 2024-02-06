from text import Text
from button import Button
# Mutliple inheritance: component class inherits from Text class and Button class.
class Component(Text, Button):
    def __init__(self, canvas):
        super(Component, self).__init__(canvas)
        self.canvas = canvas
    
    def draw_componet(self, x, y, width, height):
       self.canvas.create_rectangle(x,y, width, height)