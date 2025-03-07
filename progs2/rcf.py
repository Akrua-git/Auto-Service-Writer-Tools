import customtkinter
from datetime import date
from fillpdf import fillpdfs
import os
import win32print
import win32api
import os
    

customtkinter.set_default_color_theme("dark-blue")

today = date.today()

ctk = customtkinter

class Entryframe(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.cmile = ctk.CTkEntry(self, placeholder_text='Invoice Total')
        self.cmile.pack(padx='10', pady='5')
        global cmile
        cmile = self.cmile

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_default_color_theme("dark-blue")
        
        self.geometry('180x200')
        self.title('Print Lube Sticker')

        self.label = ctk.CTkLabel(self, text='Remove CC Fee', font=('Arial', 20))
        self.label.grid(row=0, column=0, pady='10', padx='10')


        self.frame1 = Entryframe(master=self)
        self.frame1.grid(row=1, column=0, sticky='nsew', padx='10')

        self.nbtn = ctk.CTkButton(self, text='Calculate', command=self.nextClick)
        self.nbtn.grid(row=2, column=0, sticky='nsew', padx='10', pady='10')

    def nextClick(self):
        print(cmile)

        nccfee = int(cmile.get()) * 0.029126
        totalnf = int(cmile.get()) - nccfee
        
        #self.toplevel_window = ToplevelWindow(self)
        print(totalnf)
        self.ttl = ctk.CTkLabel(self, text=f'Total: {totalnf}')
        self.ttl.grid(row=3, column=0, sticky='nsew', padx='10')
    

app = App()
app.mainloop()
