import customtkinter
from datetime import date
from fillpdf import fillpdfs
import os
import win32print
import win32api
import os
import subprocess
    

customtkinter.set_default_color_theme("dark-blue")

today = date.today()

ctk = customtkinter



class Entryframe(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.nbtn = ctk.CTkButton(self, text='Lube Sticker', command=self.lube)
        self.nbtn.pack(padx='10', pady='10')

        self.nbtn2 = ctk.CTkButton(self, text='Remove CC Fee', command=self.rcf)
        self.nbtn2.pack(padx='10', pady='10')

    def rcf(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "progs2/rcf.py"
        abs_file_path = os.path.join(script_dir, rel_path)
        os.startfile(abs_file_path)

    def lube(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "progs2/PLS/main.py"
        abs_file_path = os.path.join(script_dir, rel_path)
        os.startfile(abs_file_path)
    

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_default_color_theme("dark-blue")
        
        self.geometry('210x200')
        self.title('Print Lube Sticker')

        self.label = ctk.CTkLabel(self, text='Service Advisor Tools', font=('Arial', 20))
        self.label.grid(row=0, column=0, pady='10', padx='10', sticky='nsew')


        self.frame1 = Entryframe(master=self)
        self.frame1.grid(row=1, column=0, sticky='nsew', padx='10')


    

app = App()
app.mainloop()
