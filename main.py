#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

from text_field import TextField

WIDTH = 800
HEIGHT = 600    

class App:
    def __init__(self, width: int, height: int) -> None:
        pygame.init()

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Текстовый редактор")
        
        self.text_field = TextField()
        
        self.mainloop()

        pygame.quit()

    def mainloop(self) -> None:

        running = True
        
        while running:
            for event in pygame.event.get():
                self.text_field.event_processor(event)
                if self.text_field.need_update:
                    self.text_field.vizualize(self.window)
                    pygame.display.flip()
                    self.text_field.need_update = False
                if self.text_field.need_exit:
                    running = False


            
    
    
my_app = App(width=WIDTH, height=HEIGHT)