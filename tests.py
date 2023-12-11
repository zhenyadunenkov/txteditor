#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from tkinter import Event

from document import Document
from main import App
from nlp_magic import Summarizer

class TestDocument(unittest.TestCase):

    def test_create_doc(self):
        doc = Document()
    
    def test_get_text(self):
        doc = Document()
        doc("full")
        doc("summary")
    
    def test_update_text(self):
        doc = Document()
        doc.update_text("Тестовая строка \nЕщё одна тестовая строка","full")
        doc.update_text("Тестовая строка \nЕщё одна тестовая строка","summary")
    
    def test_remove_all(self):
        doc = Document()
        doc.remove_all()
        
    def test_update_summary(self):
        doc = Document()
        doc.update_text("Тестовая строка \nЕщё одна тестовая строка","full")
        doc.update_summary()


class TestMain(unittest.TestCase):

    def test_create_app(self):
        my_app = App("unittest")
        my_app.destroy()

    def test_change_title(self):
        my_app = App("unittest")
        mock_event = Event()
        my_app._App__change_title(mock_event)
        my_app.destroy()

    def test_clear_field(self):
        my_app = App("unittest")
        mock_event = Event()
        my_app._App__clear_field(mock_event)
        my_app.destroy()

class TestSummarizer(unittest.TestCase):
    
    def test_create_summarizer(self):
        my_summarizer = Summarizer()

    def test_availability(self):
        my_summarizer = Summarizer()
        my_summarizer.is_available()
        
    def test_summarize(self):
        my_summarizer = Summarizer()
        my_summarizer.summarize("""
                                Тестовая строка для тестирования работы суммарайзера,
                                связывающегося с веб-сервером (если он доступен),
                                выполняющим суммаризацию, или возвращающим пустую
                                строку (если веб-сервер недоступен).
                                """)
              
        
        
        
        
unittest.main(argv=[''], verbosity=2, exit=False)
