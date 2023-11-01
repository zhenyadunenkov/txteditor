#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class TextField:
    
    need_exit: bool
    
    def __init__(self, window: pygame.surface.Surface) -> None:
        self.need_exit = False

    
    def event_processor(self, event: pygame.event.Event) -> None:
        
        
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and \
            pygame.key.name(event.key) == "escape":
            self.need_exit = True

        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
    
    
    def vizualize(self) -> None:
        pass