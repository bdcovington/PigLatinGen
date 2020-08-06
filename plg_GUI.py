# plg_GUI.py

from tkinter import *
from plg_functions import PigLatin
window = Tk()
# LABEL
w = '600'
h = '275'
window.geometry('{}x{}'.format(w, h))
window.title('Pig Latin Generator')

class PigLatinGUI:

    def __init__(self):
        self.plg = PigLatin()


    def run_program(self):

        self.entry_points()
        self.buttons()
        self.note_message()

    def entry_points(self):
        self.entry_value = Entry(window, width=70, bd=4)
        self.results = Entry(window, state="disabled", width=70, bd=4)
        self.entry_value.grid(row=0, column=0, padx=85, pady=45, ipady=2)
        self.results.grid(row=1, column=0, padx=25, pady=10, ipady=5)
        self.lbl1=Label(window, text='Enter a phrase:')
        self.lbl1.place(x=600/2 -40, y=18)
        self.lbl2=Label(window, text='Result:')
        self.lbl2.place(x=600/2 -20, y=102)

    def buttons(self):
        self.translate_phrase = Button(window, text="Translate!", command=self.translate_message, padx=20, pady=15)
        self.translate_phrase.grid(row=2, column=0)

    def translate_message(self):
        self.results.config(state="normal")
        self.results.delete(0, END)
        result = self.entry_value.get()
        self.results.insert(0, self.plg.encodeit(result))
        self.results.config(state="readonly")

    def note_message(self):
        self.note = Message(window, pady=5, text="Note: Punctuation will not be tolerated!", width=300)
        self.note.grid(row=3, column=0)

if __name__ == '__main__':
    run = PigLatinGUI()
    run.run_program()
    window.mainloop()
