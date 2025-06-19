import random 
import sys, getopt, os
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from flashCard_GUI import Ui_MainWindow

repeat_cards = []
shuffled_List = []

def add_item(list, item):
	list.append(item)
	return list

class MyFlashcardProgram(Ui_MainWindow):
	def __init__(self, MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(MainWindow)
		# Connect "nextCard" button with a custom function (addInputTextToListbox) to display next card in sorted list
		self.nextCard.clicked.connect(self.addInputTextToTextDisplay)
		# Connect "nextCard" button with a custom function (addInputTextToListbox) to display next card in sorted list
		self.repeatCard.clicked.connect(self.addCurrentToRepeat)
		self.selectList.clicked.connect(self.get_file_content)
	

	def addInputTextToTextDisplay(self):
		global shuffled_List,repeat_cards
		if len(shuffled_List) > 0:
			self.new_card = shuffled_List[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			shuffled_List.remove(self.new_card)
		elif len(repeat_cards) > 0:
			self.new_card = repeat_cards[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			repeat_cards.remove(self.new_card)
			self.repeatList.clear()
			self.repeatList.addItems(repeat_cards)
		else:
			self.currentCard.clear()
			
			
	def addCurrentToRepeat(self):
		global shuffled_List,repeat_cards
		if len(shuffled_List) > 0:
			rtxt = add_item(repeat_cards, self.new_card)
			self.repeatList.clear()
			self.repeatList.addItems(rtxt)
			self.new_card = shuffled_List[0]
			self.currentCard.clear()
			self.currentCard.append(self.new_card)
			shuffled_List.remove(self.new_card)
		else:
			return

	def get_file_content(self):
		global shuffled_List,repeat_cards
		filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file')[0]
		if filename == '':
			return ''
		try:
			with open(filename, encoding='utf8') as file:
				inputfile = file.read().splitlines()
				try:
					shuffled_List = random.sample(inputfile, len(inputfile))
				except Exception as e:
					QMessageBox.warning(None, 'Can not open file', 'Can not open file {}:\n{}'.format(filename, e))
					return ''
		except IOError:
			return ''


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()

	prog = MyFlashcardProgram(MainWindow)

	MainWindow.show()
	sys.exit(app.exec_())
