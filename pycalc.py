#!/usr/bin/env python
# Author: Vishwas K Singh
# A simple calculator program in Tkinter
import os
from ttk import *
import Tkinter as tk

class Calculator(tk.Frame):

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
		self.top = self.winfo_toplevel()

		self.total=0
		self.entered_number=0
		self.operatorlist = []

		self.createWidgets()

	def createWidgets(self):
		vcmd = self.register(self.validate)
		self.entry = tk.Entry(self,validate="key", validatecommand=(vcmd, "%P"), justify=tk.RIGHT)
		
		self.total_label_text =tk.IntVar()
		self.total_label_text.set(self.total)
		self.total_label = tk.Label(self, textvariable= self.total_label_text)
		
		self.label = tk.Label(self, text='Total:')
		
		self.zeroButton = tk.Button(self, text='0', command=lambda:self.insert_number(self.zeroButton["text"]))
		self.oneButton = tk.Button(self, text='1', command=lambda:self.insert_number(self.oneButton["text"]))
		self.twoButton = tk.Button(self, text='2', command=lambda:self.insert_number(self.twoButton["text"]))
		self.threeButton = tk.Button(self, text='3', command=lambda:self.insert_number(self.threeButton["text"]))
		self.fourButton = tk.Button(self, text='4', command=lambda:self.insert_number(self.fourButton["text"]))
		self.fiveButton = tk.Button(self, text='5', command=lambda:self.insert_number(self.fiveButton["text"]))
		self.sixButton = tk.Button(self, text='6', command=lambda:self.insert_number(self.sixButton["text"]))
		self.sevenButton = tk.Button(self, text='7', command=lambda:self.insert_number(self.sevenButton["text"]))
		self.eightButton = tk.Button(self, text='8', command=lambda:self.insert_number(self.eightButton["text"]))
		self.nineButton = tk.Button(self, text='9', command=lambda:self.insert_number(self.nineButton["text"]))

		self.addButton = tk.Button(self, text='+', command=lambda:self.calculatevalue('+'))
		self.subButton = tk.Button(self, text='-', command=lambda:self.calculatevalue('-'))
		self.mulButton = tk.Button(self, text='x', command=lambda:self.calculatevalue('*'))
		self.divButton = tk.Button(self, text='/', command=lambda:self.calculatevalue('/'))
		self.eqlButton = tk.Button(self, text='=', command=lambda:self.finalresult('='))
		self.clsButton = tk.Button(self, text='C', command=lambda:self.update('C'))
		self.resetButton = tk.Button(self, text='Reset', command=lambda:self.reset('R'))
		self.decimalButton = tk.Button(self, text='.', command=lambda:self.insert_number(self.decimalButton["text"]))

		#LAYOUT
		self.entry.grid(row=1, column=0, columnspan=5,padx=3, pady=3,sticky=tk.E+tk.W)
		self.label.grid(row=0, column=0, sticky=tk.W)
		self.total_label.grid(row=0, column=1, columnspan=3, sticky=tk.E)
		
		self.oneButton.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
		self.twoButton.grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
		self.threeButton.grid(row=2, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
		self.fourButton.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
		self.fiveButton.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
		self.sixButton.grid(row=3, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
		self.sevenButton.grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
		self.eightButton.grid(row=4, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
		self.nineButton.grid(row=4, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
		self.zeroButton.grid(row=5, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

		self.addButton.grid(row=2, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
		self.subButton.grid(row=3, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
		self.mulButton.grid(row=4, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
		self.divButton.grid(row=5, column=3, sticky=tk.N+tk.S+tk.E+tk.W)
		
		self.eqlButton.grid(row=5, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
		self.clsButton.grid(row=5, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
		self.resetButton.grid(row=6, column=0, columnspan=2, sticky = tk.W+tk.E)
		self.decimalButton.grid(row=6, column=2, columnspan=2, sticky = tk.W+tk.E)

		#KEY BINDINGS
		self.top.bind('<Return>', self.returnevent)
		self.top.bind('<F1>', self.addevent)
		self.top.bind('<F2>', self.subevent)
		self.top.bind('<F3>', self.mulevent)
		self.top.bind('<F4>', self.divevent)


	def validate(self, new_text):
		if not new_text:
			self.entered_number=0
			return True
		try:
			self.entered_number = float(new_text)
			return True
		except ValueError:
			return False


	def insert_number(self, insertvalue):
		self.entry.insert(tk.END, insertvalue)

	def calculatevalue(self, method):
		self.operatorlist.append(method)
		#print self.operatorlist
		if self.operatorlist[0] == '+':
			self.total += self.entered_number
			self.displayresult()
		elif self.operatorlist[0] == '-':
			if self.total == 0:
				self.total += self.entered_number
				self.displayresult()

			else:
				self.total -= self.entered_number
				self.displayresult()

		elif self.operatorlist[0] == '*':
			if self.total == 0:
				self.total += self.entered_number
				self.displayresult()
			else:
				self.total *= self.entered_number
				self.displayresult()

		elif self.operatorlist[0] == '/':
			if self.total == 0:
				self.total += self.entered_number
				self.displayresult()
			else:
				if self.entered_number != 0:
					self.total /= self.entered_number
					self.displayresult()
				else:
					pass
		#print '1'
		#print self.operatorlist
		if len(self.operatorlist) >= 2:
			self.operatorlist.remove(self.operatorlist[0])
		
		#print self.operatorlist
	
	def displayresult(self):
		#print self.total
		self.entry.delete(0, tk.END)
		self.total_label_text.set(self.total)

	def update(self, method):
		print 'clear'
		self.entry.delete(0, tk.END)

	def reset(self, method):
		print 'reset'
		self.entry.delete(0, tk.END)

		self.total = 0
		self.entered_number = 0
		self.operatorlist = []

		self.total_label_text.set(self.total)

	def finalresult(self, method):
		#print self.total,self.entered_number
		if len(self.operatorlist) == 1:
			self.operator = self.operatorlist[0]
			if self.operator == '+':
				self.total += self.entered_number
			elif self.operator == '-':
				self.total -= self.entered_number
			elif self.operator == '*':
				self.total *= self.entered_number
			elif self.operator == '/':
				if self.entered_number !=0 :
					self.total /= self.entered_number
				else :
					self.total = 0


		self.displayresult()
	
	def returnevent(self,event):
		self.finalresult('=')
		return True
	def addevent(self, event):
		self.calculatevalue('+')
		return True

	def subevent(self, event):
		self.calculatevalue('-')
		return True

	def mulevent(self, event):
		self.calculatevalue('*')
		return True

	def divevent(self, event):
		self.calculatevalue('/')
		return True

app = Calculator()

app.master.title('Calculator')
if os.name == "nt":
	app.master.wm_iconbitmap(bitmap = "images.ico")
else:
	app.master.wm_iconbitmap(bitmap = "@images.xbm")

app.mainloop()


