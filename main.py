#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Entry, Text

GEOMETRY = "800x600"

class App:
    def __init__(self) -> None:

        self.window = Tk()
        self.window.title("Текстовый редактор")
        self.window.geometry(GEOMETRY)
        self.window.configure(bg="black")
        
        self.label = Label(text="Мы тут не шуточки шутить пришли, текст вводи!",
                           bg="black", fg="white")
        self.label.pack()
        
        self.text_field = Text(self.window, bd=1, bg="black", fg="white",
                               highlightthickness = 0, borderwidth = 0,
                               insertbackground="white")
        self.text_field.pack()
        self.text_field.focus()
        self.window.mainloop()

            
    
    
my_app = App()