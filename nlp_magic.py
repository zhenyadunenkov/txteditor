#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, error

import json


class Summarizer():
        
    def __init__(self):
        self.url = "https://z25f2-34-125-34-172.ngrok-free.app/"
        self.myurl = self.url + "json"
    
    def is_available(self) -> bool:
        try:
            req = request.urlopen(self.url)
            available = True
        except error.HTTPError:
            available = False
        return available
        
    def summarize(self, txt: str) -> str:
        msg = {"to_sum": txt}
        package = json.dumps(msg).encode('utf8')
        req = request.Request(self.myurl, 
                              data=package,
                              headers={'content-type': 'application/json'})
        
        try:
            response = request.urlopen(req)
            parsed = response.read().decode()
        except error.HTTPError:
            parsed = ""
        
        if "summarize: " in parsed:
            parsed.replace("summarize: ", "")

        return parsed

