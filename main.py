#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import customtkinter as ctk

from tkinter import Event
from document import Document


SIZE = "800x600+250+70"

class App(ctk.CTk):

    def __init__(self, aim="main") -> None:
        super().__init__()
        self.__init_gui()
        self.document = Document()
        self.level_of_editing = "full"
        
        if aim=="main":
            self.mainloop()
        else:
            pass

    def __init_gui(self) -> None:
        
        # APP WINDOW PARAMS
        ctk.set_appearance_mode("dark")
        self.title("AOTE")
        self.geometry(SIZE)
        self.last_geometry = self.winfo_geometry()
        self.bind("<Configure>", self.__change_title)
        self.bind("<Escape>", self.__quit)
        self.bind("<Control-Delete>", self.__clear_field)
        self.bind("<Control-Tab>", self.__change_mode)
        
        self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=0)
        # self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2), weight=1)
        self.iconbitmap('@/home/chbchk/txteditor/logo.xbm')
        self.iconmask('@/home/chbchk/txteditor/logo.xbm')
        
        # FONT
        custom_font = ctk.CTkFont("Ubuntu Mono", 16, 'normal')
        
        # TABS (FULL TEXT FIELD + SUMMARY FIELD CONTAINERS)
        self.tabview = ctk.CTkTabview(master=self, bg_color="#52555b", 
                                 fg_color="#52555b", corner_radius=0)
        self.tabview.grid(row=0, column=1, columnspan=2, sticky="nsew")
        
        tab_full = self.tabview.add("  Full   ")
        tab_summary = self.tabview.add(" Summary ")
        
        self.tabview._segmented_button.grid(sticky="w")
        self.tabview._segmented_button.configure(font=custom_font, 
                                            fg_color="#39414b",
                                            selected_color="#39414b",
                                            selected_hover_color="#39414b",
                                            unselected_color="#52555b",
                                            unselected_hover_color="#272d34",
                                            border_width=0,
                                            width=20,
                                            height=40,
                                            command=self.__change_mode)
        tab_full.grid_columnconfigure(0, weight=1)
        tab_full.grid_rowconfigure(0, weight=1)

        tab_summary.grid_columnconfigure(0, weight=1)
        tab_summary.grid_rowconfigure(0, weight=1)

        # FULL TEXT FIELD
        self.text_field = ctk.CTkTextbox(master=tab_full, 
                                         corner_radius=0, 
                                         wrap = "word",
                                         font=custom_font,
                                         fg_color="#39414b")
        self.text_field.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.text_field.grid_columnconfigure(0, weight=1)
        self.text_field.focus()  
        self.text_field.bind("<KeyRelease>", self.__update_document_full)


        # SUMMARY TEXT FIELD
        self.summary_field = ctk.CTkTextbox(master=tab_summary, 
                                         corner_radius=0, 
                                         wrap = "word",
                                         font=custom_font,
                                         fg_color="#39414b")
        self.summary_field.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.summary_field.grid_columnconfigure(0, weight=1)
        self.summary_field.bind("<KeyRelease>", self.__update_document_summary)



    def __change_title(self, event: Event) -> None:
        if self.winfo_geometry() != self.last_geometry:
            self.last_geometry = self.winfo_geometry()
            if self.title() != "AOTE":
                self.title("AOTE")
            else:
                self.title("Another One Text Editor")

    def __quit(self, event: Event) -> None:
        self.destroy()

    def __change_mode(self, event: Event) -> None:
        if self.tabview.get() == " Summary ":
            self.tabview.set("  Full   ")
            self.level_of_editing = "full"
            update_field = self.text_field
            self.text_field.focus()
        else:
            self.tabview.set(" Summary ")
            self.level_of_editing = "summary"
            self.document.update_summary()
            update_field = self.summary_field
            self.summary_field.focus()
            
        update_field.delete('1.0', "end")
        update_field.insert('1.0', self.document(self.level_of_editing))
        
    def __update_document_full(self, event: Event) -> None:
        if self.level_of_editing == "summary":
            return
        current_text = self.text_field.get("1.0", "end")
        self.document.update_text(current_text, "full")

    def __update_document_summary(self, event: Event) -> None:
        if self.level_of_editing == "full":
            return
        print("обновляю суммари")
        current_text = self.summary_field.get("1.0", "end")
        self.document.update_text(current_text, "summary")

    
    def __clear_field(self, event: Event) -> None:
        self.document.remove_all()
        self.text_field.delete('1.0', "end")
        self.summary_field.delete('1.0', "end")
    
  
if __name__ == "__main__":
    my_app = App()