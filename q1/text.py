class Text:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        
    #function overloading:
    # The following two functions have the same name, but takes in different number of parameters
    
    def draw_text(self, text, x, y, font):
        self.canvas.create_text(x, y, text=text, font = font)
    
    def draw_text(self, text, x, y, fill, font):
        self.canvas.create_text(x, y, text = text, fill = fill, font = font)
        
        
    