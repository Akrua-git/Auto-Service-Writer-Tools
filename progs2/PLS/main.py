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

def print_pdf_to_specific_printer(file_path, printer_name):
    # Open a handle to the printer
    printer_handle = win32print.OpenPrinter(printer_name)
    
    # Print the file using the Windows shell
    win32api.ShellExecute(0, "print", file_path, None, ".", 0)

    # Close the printer handle
    win32print.ClosePrinter(printer_handle)
    
pdf_path = r"toPrint.pdf"
printer_name = "Sticker"

def p():
    os.startfile('toPrint.pdf')



def makeLabel():
    fields = list(fillpdfs.get_form_fields('LUBE STICKER.pdf').keys())
    print(fields)

    data_dict = {
        fields[0]: nextdate1,
        fields[1]: nextmile
    }

    fillpdfs.write_fillable_pdf('LUBE STICKER.pdf', 'toPrint.pdf', data_dict)
    

class Entryframe(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.cmile = ctk.CTkEntry(self, placeholder_text='Current Mileage')
        self.cmile.pack(padx='10', pady='5')
        global cmile
        cmile = self.cmile


        self.cdate = ctk.CTkLabel(self, text=f'Current Date: {today.month}/{today.day}/{today.year}')
        self.cdate.pack(padx='10', pady='5')
            
        global switch_var
        switch_var = customtkinter.StringVar(value="off")
        switch = customtkinter.CTkSwitch(self, text="Full Synthetic",
                                     variable=switch_var, onvalue="on", offvalue="off")

        switch.pack(pady='5', padx='10')

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry('250x200')
        self.title('Print Lube Sticker')

        self.label = ctk.CTkLabel(self, text='Next Mileage:', font=('Arial', 20))
        self.label.pack(pady='10', padx='10')

        self.nml = ctk.CTkLabel(self, text=nextmile, font=('Arial', 20))
        self.nml.pack(pady='2', padx='10')

        self.label1 = ctk.CTkLabel(self, text='Next Date:', font=('Arial', 20))
        self.label1.pack(pady='10', padx='10')

        self.ndt = ctk.CTkLabel(self, text=nextdate1, font=('Arial', 20))
        self.ndt.pack(pady='2', padx='10')

        self.printB = ctk.CTkButton(self, text='Print', command=p)
        self.printB.pack()

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry('180x200')
        self.title('Print Lube Sticker')

        self.label = ctk.CTkLabel(self, text='Print Lube Sticker', font=('Arial', 20))
        self.label.grid(row=0, column=0, pady='10', padx='10')


        self.frame1 = Entryframe(master=self)
        self.frame1.grid(row=1, column=0, sticky='nsew', padx='10')

        self.nbtn = ctk.CTkButton(self, text='Next', command=self.nextClick)
        self.nbtn.grid(row=2, column=0, sticky='nsew', padx='10', pady='10')

    def nextClick(self):
        print(switch_var.get())

        global nextmile
        global nextdate1

        if switch_var.get() == 'on':
            nextmile = int(cmile.get()) + 5000
            nextdate1 = f'{today.month + 5}/{today.day}/{today.year}'
        else:
            nextmile = int(cmile.get()) + 3000
            nextdate1 = f'{today.month + 3}/{today.day}/{today.year}'

        makeLabel()

        self.toplevel_window = ToplevelWindow(self)
        print(nextmile)
    

app = App()
app.mainloop()
