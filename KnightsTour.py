#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:26:48 2019

@author: eustinakim
"""

import Tkinter as Tk

class KnightsTourGame(object):
    def __init__(self,master,n):
        self.n = n
        self.master = master
        self.canvas = Tk.Canvas(self.master, width = 500, height = 500)
        self.canvas.pack()
        self.current = [0,0]
    
        #making the grids
        for i in range(self.n):
            for j in range(self.n):
                self.canvas.create_rectangle(i*500/self.n,j*500/self.n,i*500/self.n+500/self.n,j*500/self.n+500/self.n)
        
        #set the starting square as orange
        self.canvas.create_rectangle(0,0,500/self.n,500/self.n,fill="orange")
        
        self.canvas.bind("<Button-1>", self.click)
    
    def is_validMove(self,x_new,y_new):
        x_cur = self.current[0]
        y_cur = self.current[1]
            
        if(x_new>=500 or y_new>=500):
            return False
        
        #list of possible directions
        directions = [
        [500/self.n*2, 500/self.n],
        [500/self.n, 500/self.n*2],
        [500/self.n, -500/self.n*2],
        [-500/self.n*2, 500/self.n],
        [-500/self.n, 500/self.n*2],
        [500/self.n*2, -500/self.n],
        [-500/self.n, -500/self.n*2],
        [-500/self.n*2, -500/self.n]
    ]
        
        for i in range(len(directions)):
            if x_cur + directions[i][0] == x_new and y_cur + directions[i][1] == y_new:
                return True
        return False
    
    def click(self,mouse):
        #mouse.x, mouse.y tells us the location of where you click the mouse
        x = mouse.x/(500/self.n)*(500/self.n) #points to the left top
        y = mouse.y/(500/self.n)*(500/self.n)
        #if move is valid, change the original x and y to blue and new x and y to orange
        if self.is_validMove(x,y) is True:
            #Assign appropriate colors
            self.canvas.create_rectangle(x,y,x+500/self.n,y+500/self.n, fill = "orange")
            self.canvas.create_rectangle(self.current[0],self.current[1],self.current[0]+500/self.n,self.current[1]+500/self.n,fill="blue")
            #update positions
            self.current = [x, y]
    
def knights_tour(n):
  root = Tk.Tk()
  gui = KnightsTourGame(root,n)
  root.mainloop()
        
if __name__ == "__main__":
    knights_tour(10)