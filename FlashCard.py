import random 
import sys, getopt
from PyQt5 import QtCore, QtWidgets, QtGui
from flashCard_GUI import Ui_MainWindow

with open('cardlist.txt') as f:
    	inputfile = f.read().splitlines()

shuffledList = random.sample(inputfile, len(inputfile))
print(shuffledList)
repeatcards = []

def add_item(list, item):
	list.append(item)
	return list

class MyFlashcardProgram(Ui_MainWindow):
	def __init__(self, MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(MainWindow)
		self.cardList.addItems(shuffledList)

		# Connect "nextCard" button with a custom function (addInputTextToListbox) to display next card in sorted list
		self.nextCard.clicked.connect(self.addInputTextToTextDisplay)
		# Connect "nextCard" button with a custom function (addInputTextToListbox) to display next card in sorted list
		self.repeatCard.clicked.connect(self.addCurrentToRepeat)

	def addInputTextToTextDisplay(self):
		if len(shuffledList) > 0:
			self.new_card = shuffledList[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			shuffledList.remove(self.new_card)
			self.cardList.clear()
			self.cardList.addItems(shuffledList)
		elif len(repeatcards) > 0:
			self.new_card = repeatcards[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			repeatcards.remove(self.new_card)
			self.repeatList.clear()
			self.repeatList.addItems(repeatcards)
		else:
			sys.exit()

	def addCurrentToRepeat(self):
		if len(shuffledList) > 0:
			rtxt = add_item(repeatcards,self.new_card)
			self.repeatList.clear()
			self.repeatList.addItems(rtxt)
			self.new_card = shuffledList[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			shuffledList.remove(self.new_card)
			self.cardList.clear()
			self.cardList.addItems(shuffledList)
		else:
			return

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()

	prog = MyFlashcardProgram(MainWindow)

	MainWindow.show()
	sys.exit(app.exec_())
