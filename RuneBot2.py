# -*- coding: utf-8 -*-
"""
Created on Mon May 22 00:33:21 2017

@author: Supreme Ruler
"""
import actions as act

task = int(input("Choose task: Fletching(1), Alchemy(2), Runemelt(3): "))

if task ==1:
    x = int(input("How many feathers? (will be converted to multiple of 150): "))
    y = x/150 #making sure a multiple of 150 is inserted into fletching()
    z = y*150
    print("will process ",z,"feathers")
    act.fletching(z)
elif task == 2:
    x2 = int(input("how many items to alch?: "))
    act.alchemy(x2)
elif task == 3:
    x3 = int(input("how many ores to melt? (will be converted to multiple of 3): "))
    y3 = x3/3
    z3 =3*y3
    print("will melt ",int(z3),"ores")
    act.runemelt(int(z3))
else:
    print("invalid input, press any key to terminate and try again")
    input()
    exit()


