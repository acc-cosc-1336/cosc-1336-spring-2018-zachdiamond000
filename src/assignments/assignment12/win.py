from tkinter import Tk
from converter import Converter
from tkinter.ttk import Label

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('Tk')
        self.geometry('640x480')
        self.label1 = Label(self, text='Km: 100').grid(row=0, column=1)
        

        self.converter = Converter()
        
        self.label2 = Label(self, text= 'Miles: ' + str(self.converter.get_miles_from_km(100))).grid(row=1, column=1)
        

        
        self.mainloop()
