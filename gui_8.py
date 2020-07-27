from tkinter import *

class KrissButtons:

	def_init_(self, master):
	frame = Frame(master)
	frame.pack()
	
	self.printButton = Button(frame, text="Printe Message", command=self.printMessage)
	self.printButton.pack(side=LEFT)
	
	self.quitButton = Button(frame, text="Quit", command=frame.quit)
	self.quitButton.pac(side=LEFT)
	
	
	def printMessage(self):
	print("This is, something else!")
	
	root = Tk()
	b = KrissButtons(root)
	root.mainloop()