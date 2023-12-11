#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from nlp_magic import Summarizer
from singleton import Singleton

class Document(Singleton):
    
    def init(self) -> None:
        self.__marked_text = defaultdict(lambda: {"summary needs update": False,
                                "summary": "",
                                "full": ""})
        self.summary_overflow = False
        self.summarizer = Summarizer()
        
    def __init__(self) -> None:
        pass

    def __call__(self, level_of_editing: str="full") -> str:
        text = ""
        for i in range(len(self.__marked_text)):
           text += self.__marked_text[i][level_of_editing] + "\n"
        return text
        

    def update_text(self, entry: str, level_of_editing: str) -> None:
        paragraphs = entry.splitlines()
        
        if level_of_editing == "full":
            for i in range(len(paragraphs)):
                if paragraphs[i] == "":
                    self.__marked_text[i]["full"] = ""
                    self.__marked_text[i]["summary"] = ""
                    self.__marked_text[i]["summary needs update"] = False
                    
                if paragraphs[i] != self.__marked_text[i]["full"]:
                    self.__marked_text[i]["full"] = paragraphs[i]
                    if len(paragraphs[i]) > 150:
                        self.__marked_text[i]["summary needs update"] = True
                    else:
                        self.__marked_text[i]["summary"] = paragraphs[i]
                        self.__marked_text[i]["summary needs update"] = False
            if len(self.__marked_text) > len(paragraphs):
                for i in range(len(paragraphs), len(self.__marked_text)):
                    self.__marked_text[i]["summary needs update"] = False
                    self.__marked_text[i]["summary"] = ""
                    self.__marked_text[i]["full"] = ""
        
        else:
            for i in range(len(paragraphs)):
                if paragraphs[i] != self.__marked_text[i]["summary"]:
                    self.__marked_text[i]["summary"] = paragraphs[i]
        
        self.__delete_empty_strings()
        self.__normalize_summary()
                
    def remove_all(self) -> None:
        self.__marked_text = defaultdict(lambda: {"summary needs update": False,
                                "summary": "",
                                "full": ""})

    def update_summary(self) -> None:
        
        if self.summarizer.is_available():
            for i in range(len(self.__marked_text)):
                if self.__marked_text[i]["summary needs update"]:
                    self.__marked_text[i]["summary"] = \
                        self.summarizer.summarize(self.__marked_text[i]["full"])
                    self.__marked_text[i]["summary needs update"] = False
        else:
            pass
        self.__normalize_summary()
    
    def __delete_empty_strings(self):
        for element in range(len(self.__marked_text), -1, -1):
            if self.__marked_text[element]["full"] != "":
                break
            if self.__marked_text[element]["full"] == "":
                if self.__marked_text[element]["summary"] == "":
                    del self.__marked_text[element]

        
    def __normalize_summary(self) -> None:
        for i in range(len(self.__marked_text)):
            self.__marked_text[i]["summary"] = \
                self.__marked_text[i]["summary"].replace("( )+`", "")
            
            summary = self.__marked_text[i]["summary"]
            full = self.__marked_text[i]["full"]
                        
            if len(summary) < len(full):
                offset = (len(full) - len(summary)) // 2
                self.__marked_text[i]["summary"] += " " + " `" * offset

doc1 = Document()
doc2 = Document()

doc1.update_text("dfgdfgfdgfdg", "full")
print(doc2("full"))