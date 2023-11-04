#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Word:

    paragraph: int
    
    def __init__(self, paragraph: int) -> None:
        self.content = ""
        self.paragraph = paragraph
    
    def add_char(self, char: str):
        if char == "space":
            char = " "
        self.content += char

    def remove_char(self):
        if len(self.content) > 0:
            self.content = self.content[0:-1]

    def __str__(self):
        return self.content
        