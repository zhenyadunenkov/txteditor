#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from word import Word

class TextField:
    
    need_exit: bool
    need_update: bool
    field: list[Word]
    
    def __init__(self) -> None:
        self.need_exit = False
        self.need_update = False
        self.shift_down = False
        self.alt_down = False
        
        self.__init_languages__()
        
        self.field = []
        self.current_paragraph = 0
        self.current_word = Word(self.current_paragraph)
        
        self.field.append(self.current_word)
        
    def __init_languages__(self) -> None:
        self.txt_keys = "1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./`"
        
        eng = "1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./`"
        rus = "1234567890-=йцукенгшщзхъфывапролджэ\ячсмитьбю.ё"
        self.eng_rus = {eng[x]: rus[x] for x in range(len(eng))}
        self.languages = ("eng", "rus")
        self.current_language = 0
        
        low = "1234567890-=[];',./"
        up = "!@#$%^&*()_+{}:\"<>?"
        self.eng_upper_table = {low[x]: up[x] for x in range(len(low))}
        
        low = "1234567890-=\."
        up = '!\"№;%:?*()_+/,'
        self.rus_upper_table = {low[x]: up[x] for x in range(len(low))}
        
        self.upper_table = {"eng": self.eng_upper_table, 
                            "rus": self.rus_upper_table}
    
    def event_processor(self, event: pygame.event.Event) -> None:

        # запрос на выход из программы
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
            pygame.key.name(event.key) == "escape":
            self.need_exit = True
        
        # обработка шифта и альта
        
        elif event.type == pygame.KEYDOWN and \
            pygame.key.name(event.key) == "left shift":
                self.shift_down = True
        elif event.type == pygame.KEYUP and \
            pygame.key.name(event.key) == "left shift":
                self.shift_down = False

        elif event.type == pygame.KEYDOWN and \
            pygame.key.name(event.key) == "left alt":
                self.alt_down = True
        elif event.type == pygame.KEYUP and \
            pygame.key.name(event.key) == "left alt":
                self.alt_down = False

        # добавил капслок на всякий случай 
        elif event.type == pygame.KEYDOWN and \
            pygame.key.name(event.key) == "caps lock":
                self.__change_language__()


        # обработка остальных нажатий
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            self.__text_swallover__(key)
            self.need_update = True

        # обработка запроса на смену языка
        if self.shift_down and self.alt_down:
            self.__change_language__()

    
    def __text_swallover__(self, key: str) -> None:
        if key in self.txt_keys:
            if self.languages[self.current_language] == "eng":
                if self.shift_down:
                    key = self.__uppercase__(key)
                self.current_word.add_char(key)
                
            else:
                language = self.languages[self.current_language]
                key = self.__translate__(key, language)
                if self.shift_down:
                    key = self.__uppercase__(key)
                self.current_word.add_char(key)

        elif key == "backspace":
            # ДОБАВИТЬ ОБРАБОТКУ ВЫХОДА НА ПРЕДЫДУЩИЕ СЛОВА
            # И УДАЛЕНИЕ СЛОВ, В ОБЩЕМ-ТО ТОЖЕ
            self.current_word.remove_char()

        elif key == "space":
            self.current_word = Word(self.current_paragraph)
            self.field.append(self.current_word)

        elif key == "return":
            self.current_paragraph += 1
            self.current_word = Word(self.current_paragraph)
            self.field.append(self.current_word)
            
        # ДОБАВИТЬ ОБРАБОТКУ КЛАВИШ ПЕРЕМЕЩЕНИЯ КУРСОРА (И КУРСОР БЫ, КОНЕЧНО)

    def __change_language__(self) -> None:
        if self.current_language == 0:
            self.current_language = 1
        else:
            self.current_language = 0
            
    def __uppercase__(self, char: str) -> str:
        # здесь же будет обработка языка
        if self.languages[self.current_language] == "eng":
            if char in "qwertyuiopasdfghjklzxcvbnm ":
                return char.upper()
            else:
                return self.upper_table["eng"][char]
        if self.languages[self.current_language] == "rus":
            if char in "йцукенгшщзхъфывапролджэячсмитьбюё ":
                return char.upper()
            else:
                return self.upper_table["rus"][char]
    
    def __translate__(self, key, language) -> str:
        key = self.eng_rus[key]
        return key             
        
    def vizualize(self, window: pygame.surface.Surface) -> None:
        
        window.fill((0, 0, 0))
        
        my_font = pygame.font.SysFont("Sans", 15)
        
        x = 10
        y = 10
        
        space_length = 10
        
        last_paragraph = 0
        
        for word in self.field:
            
            if word.paragraph != last_paragraph:
                x = 10
                y += 20
                last_paragraph = word.paragraph
            
            text_surface = my_font.render(str(word), False, (255, 255, 255))
            window.blit(text_surface, (x, y))
            
            word_length = text_surface.get_width()
            
            x += word_length + space_length
            
            
        
