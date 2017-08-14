# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:33:21 2017

@author: Supreme Ruler
"""
import pyautogui as gui
import randtime as rt

def click():
    """clicks left mouse button in for time period around 0.2s"""
    gui.mouseDown() # mouseclick
    rt.wait(0.2)    
    gui.mouseUp()
    return
        
    

