# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:33:21 2017

@author: Supreme Ruler
"""
import time
import random

def sig(a,b):
    """makes a random sigma between values a and b"""
    sig = random.uniform(a,b)
    return sig

def mu(a,b):
    """makes a random sigma between values a and b"""
    mu =random.uniform(a,b)
    return mu

##-----------------------------------------------------------------------------

def rtime(secs):
     """Values describing gauss distribution around given value will be outputed"""
     sec = float(secs)
     randsec = random.gauss(mu((sec-(sec/10)),(sec+(sec/10))),sig((sec-(sec/10))/10,(sec+(sec/10))/10))
     #looks messy, but for sec = 10
     #mu = something between 9 and 11, sigma = something between 9/10 and 11/10
     #randsec = value taken from distribution X with mean mu() and distribution sig()
     return randsec
 
def wait(sec):
    """waits for input amount of seconds, random gauss distribution of time is calculated"""
    time.sleep(rtime(sec))
    return


    







