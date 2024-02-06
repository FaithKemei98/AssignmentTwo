

class Button:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        
        # abstraction. The following field will be abstracted by this class Button, its an implementation detail and wont be 
        #accessed this class
        self.__color = "black"
        self.color = self.__color
        
    def draw_button(self,x,y,z,w):
        self.x = int((x + z)/2)
        self.y = int((y + w)/2)
        self.l = self.x + 30
        self.h = self.y -15
        self.canvas.create_polygon(self.x, self.y, self.x, self.y-30,self.l ,self.h)