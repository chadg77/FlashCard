FlashCard.py

- Imports Qt gui.py file flashCard_GUI created through QTDesigner and pyuic5.exe to convert to .ui to .py file
- imports and creates a list from cardlist.txt
- pulls index 0 value from a shuffled list, as cards are displayed (Next Card button) they are removed from the original shuffled list
- repeat card adds current card to repeatcards list
- once both shuffled and repeatcard list contain no more items, application closes.