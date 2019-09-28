import random 
import sys, getopt, os
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from flashCard_GUI import Ui_MainWindow

with open('cardlist.txt', encoding='utf8') as f:
    	inputfile = f.read().splitlines()

shuffledList = random.sample(inputfile, len(inputfile))
print(shuffledList)
repeatcards = []

TICK_TIME = 2**6

def add_item(list, item):
	list.append(item)
	return list

class MyFlashcardProgram(Ui_MainWindow):
	def __init__(self, MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(MainWindow)
		#self.cardList.addItems(shuffledList)

		# Connect "nextCard" button with a custom function (addInputTextToListbox) to display next card in sorted list
		self.nextCard.clicked.connect(self.addInputTextToTextDisplay)
		# Connect "nextCard" button with a custom function (addInputTextToListbox) to display next card in sorted list
		self.repeatCard.clicked.connect(self.addCurrentToRepeat)
		#added for app timer
		self.start.clicked.connect(self.do_start)
		self.timer = Qt.QTimer()
		self.timer.setInterval(TICK_TIME)
		self.timer.timeout.connect(self.tick)
		self.time = 0

	def addInputTextToTextDisplay(self):
		if len(shuffledList) > 0:
			self.new_card = shuffledList[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			shuffledList.remove(self.new_card)
			#self.cardList.clear()
			#self.cardList.addItems(shuffledList)
		elif len(repeatcards) > 0:
			self.new_card = repeatcards[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			repeatcards.remove(self.new_card)
			self.repeatList.clear()
			self.repeatList.addItems(repeatcards)
		else:
			self.timer.stop()
			self.currentCard.clear()
			
			
	def addCurrentToRepeat(self):
		if len(shuffledList) > 0:
			rtxt = add_item(repeatcards,self.new_card)
			self.repeatList.clear()
			self.repeatList.addItems(rtxt)
			self.new_card = shuffledList[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			shuffledList.remove(self.new_card)
			#self.cardList.clear()
			#self.cardList.addItems(shuffledList)
		else:
			return

	def display(self):
		self.lcd.display("%d:%2d" % (self.time // 60, self.time % 60))


	def tick(self):
		self.time += TICK_TIME/1000
		self.display()

	def do_start(self):
		if len(shuffledList) > 0:
			self.timer.start()
			self.start.setText("Started...")
			self.start.clicked.disconnect()
			self.new_card = shuffledList[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			shuffledList.remove(self.new_card)
			#self.cardList.clear()
			#self.cardList.addItems(shuffledList)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()

	prog = MyFlashcardProgram(MainWindow)

	MainWindow.show()
	sys.exit(app.exec_())
