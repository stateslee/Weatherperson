# coding: utf-8

# In[3]:


import sys
import random
#from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
 #                              QVBoxLayout, QWidget)
#from PySide2.QtCore import Slot, Qt

#initial graphics
from tkinter import *

#this is to gather the weather information
import pyowm

#setup
window = Tk()
window.geometry('350x200')
window.title ("Weather") #should eventually include pulled date and time

owm = pyowm.OWM('5bd7229ebad93b82e26d9cf4d86f9c73')

observation = owm.weather_at_place("London,UK")



t = observation.get_weather()
temp = t.get_temperature('fahrenheit') #need to grab 

observation2 = owm.weather_at_place("Charlotte,NC,USA")

t2 = observation2.get_weather()
temp2 = t2.get_temperature('fahrenheit')


lbl = Label(window, text=("London", temp), font=("Arial Bold", 12))
lbl.grid(column=0, row=0)

window.mainloop()

#print(t)
#print("London: ", temp)
#print(t2)
#print("Charlotte: ", temp2)








