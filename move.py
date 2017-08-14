# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:33:21 2017

@author: Supreme Ruler
"""

import pyautogui as gui
import randtime as rt
import random


"""
print "pick starting position"
rt.wait(5)
(xstart,ystart) = gui.position()
print "start position is", (xstart,ystart)

print "pick ending position"
rt.wait(5)
(xend,yend) = gui.position()
print "end position is", (xend,yend)
rt.wait(5)
"""
#Functions available:
    #-move1
    #-move2
    #-move3
    #-move4
    #-randmove



def move1(xstart,ystart,xend,yend,stdev,duration):
    """Moves from start to end and makes 1 variable bend"""  
    xpos1 =(xend+xstart)/2
    
    ypos1 =(yend+ystart)/2
           
    dura = float(duration)/2
        
    gui.moveTo(random.gauss(xpos1,stdev),random.gauss(ypos1,stdev), rt.rtime(dura),gui.easeInCubic)
    #print gui.position()
    
    gui.moveTo(xend,yend,rt.rtime(dura),gui.easeOutQuad)
    #print gui.position()
    
def move2(xstart,ystart,xend,yend,stdev,duration):
    """Moves from start to end and makes 2 variable bends"""  
    xpos1 =(xend+xstart)/2
    xpos2 =(xend+xpos1)/2

    ypos1 =(yend+ystart)/3
    ypos2 =(yend+ypos1)/2
           
    dura = float(duration)/3
        
    gui.moveTo(random.gauss(xpos1,stdev),random.gauss(ypos1,stdev), rt.rtime(dura),gui.easeInCubic)
    #print gui.position()
    
    gui.moveTo(random.gauss(xpos2,stdev),random.gauss(ypos2,stdev), rt.rtime(dura))
    #print gui.position()
    
    gui.moveTo(xend,yend,rt.rtime(dura),gui.easeOutQuad)
    #print gui.position()

def move3(xstart,ystart,xend,yend,stdev,duration):
    """Moves from start to end and makes 3 variable bends"""  
    xpos1 =(xend+xstart)/2
    xpos2 =(xend+xpos1)/2
    xpos3 =(xend+xpos2)/2

    ypos1 =(yend+ystart)/2
    ypos2 =(yend+ypos1)/2
    ypos3 =(yend+ypos2)/2
           
    dura = float(duration)/4
        
    gui.moveTo(random.gauss(xpos1,stdev),random.gauss(ypos1,stdev), rt.rtime(dura),gui.easeInCubic)
    #print gui.position()
    
    gui.moveTo(random.gauss(xpos2,stdev),random.gauss(ypos2,stdev), rt.rtime(dura))
    #print gui.position()
    
    gui.moveTo(random.gauss(xpos3,stdev),random.gauss(ypos3,stdev), rt.rtime(dura))
    #print gui.position()
    
    gui.moveTo(xend,yend,rt.rtime(dura),gui.easeOutQuad)
    #print gui.position()
    

def move4(xstart,ystart,xend,yend,stdev,duration):
    """Moves from start to end and makes 3 variable bends"""  
    xpos1 =(xend+xstart)/2
    xpos2 =(xend+xpos1)/2
    xpos3 =(xend+xpos2)/2
    xpos4 =(xend+xpos3)/2

    ypos1 =(yend+ystart)/2
    ypos2 =(yend+ypos1)/2
    ypos3 =(yend+ypos2)/2
    ypos4 =(yend+ypos3)/2       
           
    dura = float(duration)/5
        
    gui.moveTo(random.gauss(xpos1,stdev),random.gauss(ypos1,stdev), rt.rtime(dura),gui.easeInCubic)
    #print gui.position()
    
    gui.moveTo(random.gauss(xpos2,stdev),random.gauss(ypos2,stdev), rt.rtime(dura))
    #print gui.position()
    
    gui.moveTo(random.gauss(xpos3,stdev),random.gauss(ypos3,stdev), rt.rtime(dura))
    #print gui.position()
    
    gui.moveTo(random.gauss(xpos4,stdev),random.gauss(ypos4,stdev), rt.rtime(dura))
    #print gui.position()
    
    gui.moveTo(xend,yend,rt.rtime(dura),gui.easeOutQuad)
    #print gui.position()

def randmove(xstart,ystart,xend,yend,stdev,duration):
    x = random.random()
    
    if x<0.25:
        move1(xstart,ystart,xend,yend,stdev,duration)
        #print "1"
    elif x>=0.25 and x <= 0.50:
        move2(xstart,ystart,xend,yend,stdev,duration)
        #print "2"
    elif x>0.50 and x <= 0.75:
        move3(xstart,ystart,xend,yend,stdev,duration)
        #print "3"
    else:
        move4(xstart,ystart,xend,yend,stdev,duration)
        #print "4"
        

    
    
