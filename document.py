#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import defaultdict

class Document:
    
    def __init__(self) -> None:
        self.__marked_text = defaultdict(lambda: {"summary needs update": False,
                                "summary": "",
                                "full": ""})

    def get_text(self, level_of_editing: str) -> str:
        text = ""
        for i in range(len(self.__marked_text)):
           text += str(i) + ": " + self.__marked_text[i][level_of_editing] + "\n"
        return text
    
    def update_text(self, entry: str, level_of_editing: str) -> None:
        
        if level_of_editing in ("full", "summary"):
            paragraphs = entry.splitlines()
            self.__update_marked_text(paragraphs, level_of_editing)            

        if level_of_editing == "paragraph":
            # уточняем номер параграфа 
            num = 0 # должно быть get_paragraph_number() из гуи
            self.__update_marked_paragraph(num, entry)            
              
    def __update_marked_text(self, paragraphs: list[str], 
                             level_of_editing: str) -> None:
      
        for i in range(len(paragraphs)):
            if paragraphs[i] != self.__marked_text[i][level_of_editing]:
                if level_of_editing == "summary" and \
                    self.__marked_text[i]["full"] == "":
                        continue
                self.__marked_text[i][level_of_editing] = paragraphs[i]
                if level_of_editing == "full":
                    self.__marked_text[i]["summary needs update"] = True
        
        if len(paragraphs) < len(self.__marked_text):
            for i in range(len(paragraphs), len(self.__marked_text)):
                del self.__marked_text[i]
        
    def __update_marked_paragraph(self, paragraph_num: int,
                                  paragraph: str) -> None:
        print("paragraph modified")

