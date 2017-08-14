# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:33:21 2017

@author: Supreme Ruler
"""
import click as mouse
import keypress as kb
import move as mv
import pyautogui as gui
import randtime as rt
import random


def fletching(n):
    """function that presses 1 and space with waiting time for n-amount of cycles"""

    print("Get ready, fletching will start in 10s")
    rt.wait(10)
    
    print("starting...")
    
    for i in range((n/150)):
        
        process = (float(i)*150+150)/float(n)*100 #calculate percentage till done
        eta = (16*n/150)-16*i-16 #calculate time till done (assumption:average cycle = 16s)

        kb.press("1",0.2)
        rt.wait(1)
        kb.press("space",0.2)
        rt.wait(10)
        #USER update on progress:
        #Process: 0.00% ETA: 00s -- 00min

        print("PROCESS: ", '%.2f' % process,"% ", "ETA: ", int(eta)/3600, "hour",int(eta)/60-((int(eta)/3600)*60),"min",int(eta)%60,"sec")


def runemelt(n):
    """function that presses 1 and mouseclick with waiting time for n-amount of cycles"""

    print ("place mouse at bank position, will document in 5s") #Determine bank position
    rt.wait(5)
    bank_position = gui.position()
    (xbank, ybank) = bank_position #assign seperate paramaters to positions so we can randomize them
    print ("Bank position = ", bank_position)
    
    print ("place mouse at last ore position, will document in 5s") #Determine 3rd ore position
    rt.wait(5)
    ore_position = gui.position()
    (xore,yore) = ore_position
    print( "last ore position = ", ore_position)

    print ("get ready, melting will begin in 5s")
    rt.wait(5)

    for i in range(int(n/3)+1):
        randxbank = int(random.gauss(xbank,15))
        randybank = int(random.gauss(ybank,15))
        randxore = int(random.gauss(xore,5))
        randyore = int(random.gauss(yore,5))
      
        process = float(i+1)/float(n/3)*100  #calculate percentage till done
        eta = (n/3)*11 - i*11     

        mv.randmove(randxore,randyore,randxbank,randybank,10,0.5) #Move to bank
        rt.wait(0.1)
                   
        mouse.click() #click mouse
        rt.wait(0.5)

        kb.press("2",0.2) #press 2

        mv.randmove(randxbank,randybank,randxore,randyore,10,0.5) #move to ore position
        rt.wait(0.7)
        
        for i in range(3): #three times

            kb.press("2",0.2) #press 2
            rt.wait(0.3)

            mouse.click() #click mouse
            rt.wait(1)

        #USER update on progress:
        #Process: 0.00% ETA: 00hour 00min 00s

        print ("PROCESS: ", '%.2f' % process,"% ", "ETA: ", int(int(eta)/3600), "hour",int(int(eta)/60-((int(eta)/3600)*60)),"min",int(eta)%60,"sec")
        

def alchemy(n):
    """function that presses moves mouse to bank and inventory and presses 2 and mouseclick for n-amount of cycles"""

    print ("Get ready, alchemy will start in 10s")
    rt.wait(10) # 10s pause to get everything in position
    
    print ("starting...")
    
    for i in range(n): #repeat for n iterations

        process = float(i)/float(n)*100 #calculate percentage till done
        eta = n*3.3-i*3.3 #calculate time till done (assumption:average cycle = 3.3s)

        kb.press("1",0.2) #press 1
        rt.wait(0.5)

        mouse.click() #mouse click
        rt.wait(1.2)
        
        #USER update on progress:
        #Process: 0.00% ETA: 00hour 00min 00s

        print ("PROCESS: ", '%.2f' % process,"% ", "ETA: ", int(eta)/3600, "hour",int(eta)/60-((int(eta)/3600)*60),"min",int(eta)%60,"sec")


