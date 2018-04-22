from tkinter import Tk, Button, Label
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('Tk')
        
        
        self.display_conversation_button = Button(self, text='Display Conversation', \
                                                  command = self.display_conversation).grid(row=2, column=0)
        self.quit_button = Button(self, text='Exit the Simulation', command=self.destroy).grid(row=2, column=1)

        
        self.mainloop()

    def display_conversation(self):
        
        self.label1 = Label(self, text='Km: 100').grid(row=0, column=0)
        self.converter = Converter()
        self.label2 = Label(self, text= self.converter.get_miles_from_km(100)).grid(row=1, column=0)
