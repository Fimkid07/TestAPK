import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color

class SetupPlanner(BoxLayout):
	pass
	
class MyApp(App):

	windowSize = Window.size
	windowSizeX = float(windowSize[0])
	windowSizeY = float(windowSize[1])

	phi  =  ((1+(5**(1/2)))/2)
	Size1 = windowSizeX * (1/(phi**(1)))
	Size2 = windowSizeX * (1/(phi**(2)))
	Size3 = windowSizeX * (1/(phi**(3)))
	Size4 = windowSizeX * (1/(phi**(4)))
	Size5 = windowSizeX * (1/(phi**(5)))
	colorBackground1 = tuple(Color(225/360,19/100,8/100, mode='hsv').rgba)
	def build(self):
		return SetupPlanner()
	
if __name__ == '__main__':
	MyApp().run()