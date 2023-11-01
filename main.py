#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from text_field import TextField

WIDTH = 1024
HEIGHT = 768

class App:
    def __init__(self, width: int, height: int) -> None:
        pygame.init()

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Текстовый редактор")
        
        self.text_field = TextField(self.window)
        
        self.mainloop()

        pygame.quit()

    def mainloop(self) -> None:

        running = True
        
        while running:
            for event in pygame.event.get():
                self.text_field.event_processor(event)
                self.text_field.vizualize()
                if self.text_field.need_exit:
                    running = False


            
    
    
my_app = App(width=WIDTH, height=HEIGHT)