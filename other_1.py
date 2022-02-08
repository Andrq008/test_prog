import tkinter as tk
from tkinter import *
#from graph import *
print("Enter x, y")
x = int(input("x = "))
y = int(input("y = "))
def frame():
    penColor('black')
    brushColor('green')
    rectangle(x,y,x+100,x+100)
def roof():
    penColor('black')
    brushColor('brown')
    polygon( [(90,100), (150,50),(210,100),(90,100)])
def window():
    penColor('white')
    penSize(3)
    brushColor('black')
    rectangle(120,120,150,170)
    line(120,140,150,140)
    line(135,140,150,170)
def home(x, y):
    frame(x, y)
    roof()
    window()