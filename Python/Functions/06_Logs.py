# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:52:56 2022

@author: Krystian
"""

import datetime
import time

print(datetime.datetime.utcnow())

def log(message, dt = datetime.datetime.utcnow):
    print(dt(), message)
    
log('Uruchomienie systemu.')

def logs(*args):
    for command in args:
        log(command)
        time.sleep(1)
        
logs('Uruchomienie systemu', 'Logowanie', 'Restart', 'Wylogowanie',
     'Zamknięcie systemu')