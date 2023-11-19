#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Label, Entry, Text, Button, Event
from document import Document


SIZE = "800x600"

class App:

    def __init__(self) -> None:
        self.__init_document()
        self.__init_gui()        
        self.__app_loop()
        
    def __init_document(self) -> None:
        self.document = Document()
        self.level_of_editing = "full"

    def __init_gui(self) -> None:
        # WINDOW
        self.window = Tk()
        self.window.title("Текстовый редактор")
        self.window.geometry(SIZE)
        self.window.configure(bg="black")
        self.window.bind("<Escape>", self.__quit)

        # TEXT LABELS
        self.hint = Label(text="Вводи текст в окошке ниже!",
                           bg="black", fg="white")
        self.hint.pack()
        
        self.level = Label(text="Уровень работы с текстом: весь текст",
                           bg="black", fg="white")
        self.level.pack()

        
        # BUTTONS
        self.button_less = Button(text="less")
        self.button_less.config(command=self.__summarize)
        self.button_less.pack()

        self.button_more = Button(text="more")
        self.button_more.config(command=self.__expand)
        self.button_more.pack()
        
        # ENTRY FIELD
        self.text_field = Text(self.window, bd = 1, bg = "black", fg = "white",
                               highlightthickness = 0, borderwidth = 0,
                               insertbackground = "white",
                               wrap = "word")
        self.text_field.pack()
        self.text_field.bind("<KeyRelease>", self.__update_text)
        self.text_field.focus()
        
        
        # DEBUG TEXT
        self.current_txt = Text(self.window, bg = "black", fg = "white",
                               highlightthickness = 0, borderwidth = 0,
                               insertbackground = "white",
                               wrap = "word")
        self.current_txt.configure(state="disabled")
        self.current_txt.pack()
        self.current_txt.insert("1.0", "popop")
                                
    def __app_loop(self) -> None:
        self.window.mainloop()
        
    def __summarize(self) -> None:
        print("text is summed up")
    
    def __expand(self) -> None:
        print("text is expanded")

    def __quit(self, event: Event) -> None:
        self.window.destroy()
        
    def __update_text(self, event: Event) -> None:
        current_text = self.text_field.get("1.0", "end-1c")
        self.document.update_text(current_text, self.level_of_editing)
        
        self.current_txt.configure(state="normal")
        self.current_txt.delete('1.0', "end")
        self.current_txt.insert('1.0', self.document.get_text(self.level_of_editing))
        self.current_txt.configure(state="disabled")
    
my_app = App()