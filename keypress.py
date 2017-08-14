# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:33:21 2017

@author: Supreme Ruler
"""

import pyautogui as gui
import randtime as rt

def press(key,duration):
    """Presses a given key for given duration"""
    gui.keyDown(key)
    rt.wait(duration)    
    gui.keyUp(key)
    return


