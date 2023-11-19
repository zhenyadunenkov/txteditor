#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

class Document:
    
    def __init__(self) -> None:
        self.text = ""
        self.__marked_text = {0: {"summary needs update": False,
                                "summary": "",
                                "full": ""}}

    def __str__(self) -> str:
        return self.text

    def update_text(self, entry: str, level_of_editing: str) -> None:
        
        if level_of_editing in ("full", "summary"):
            paragraphs = self.__parse_paragraphs(entry)
            self.__update_marked_text(paragraphs, level_of_editing)            
            print("\n\n\n\n")
            print(paragraphs)

        if level_of_editing == "paragraph":
            # уточняем номер параграфа 
            num = 0 # должно быть get_paragraph_number() из гуи
            self.__update_marked_paragraph(num, entry)            
            
    def __parse_paragraphs(self, text) -> list[str]:
        return re.split('\n(?=[^\n\b])', text)
    
    def __update_marked_text(self, paragraphs: list[str], 
                             level_of_editing: str) -> None:
        
        print("updated summary or full paragraph by paragraph and hit triggers if necessary")
    
    def __update_marked_paragraph(self, paragraph_num: int,
                                  paragraph: str) -> None:
        print("paragraph modified")

