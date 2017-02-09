#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
from functools import partial
from PyQt5.QtWidgets import ( QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QGroupBox, QMessageBox, QCheckBox, QListWidget)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

def call_player(players):
    	rand_int = random.randint(0,len(players) - 1)
    	return players.pop(rand_int)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(300,300,290,230)
        self.setWindowTitle('Input Dialog')
        self.setWindowIcon(QtGui.QIcon('chip_icon_normal.png'))
    	# UnComment to use a textbox instead of checkboxes. 
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 50)
        self.textbox.resize(240,20)
        self.textbox.setText("Who's Playing?")
        self.textbox.hide()
    	
    	# Comment up until the dashed line iff you uncomenter the textbook.
        self.players = []
        self.chkbxs = []
        
        self.modCb = QCheckBox('Custom', self)
        self.modCb.move(0,10)
        self.modCb.stateChanged.connect(self.hideAllButtons)


        #------------------------------------------------------------#
        self.YousCb = QCheckBox('Youssef', self)
        self.YousCb.move(0,50)
        self.YousCb.stateChanged.connect(partial(self.addPlayers, "Youssef" ))
        self.chkbxs.append(self.YousCb)

        self.NoahCb = QCheckBox('Noah',self)
        self.NoahCb.move(75,50)
        self.NoahCb.stateChanged.connect(partial(self.addPlayers, "Noah" ))
        self.chkbxs.append(self.NoahCb)

        self.RickyCb = QCheckBox('Ricky', self)
        self.RickyCb.move(150, 50)
        self.RickyCb.stateChanged.connect(partial(self.addPlayers, "Ricky" ))
        self.chkbxs.append(self.RickyCb)

        self.DavidCb = QCheckBox('David',self)
        self.DavidCb.move(225,50)
        self.DavidCb.stateChanged.connect(partial(self.addPlayers, "David" ))
        self.chkbxs.append(self.DavidCb)

        self.DrassCb = QCheckBox('Drass', self)
        self.DrassCb.move(0,90)
        self.DrassCb.stateChanged.connect(partial(self.addPlayers, "Drass" ))
        self.chkbxs.append(self.DrassCb)

        self.LucaCb = QCheckBox('Luca',self)
        self.LucaCb.move(75,90)
        self.LucaCb.stateChanged.connect(partial(self.addPlayers, "Luca" ))
        self.chkbxs.append(self.LucaCb)

        self.SantiCb = QCheckBox('Santi',self)
        self.SantiCb.move(150,90)
        self.SantiCb.stateChanged.connect(partial(self.addPlayers, "Santi" ))
        self.chkbxs.append(self.SantiCb)

        self.AlexCb = QCheckBox('Jonah',self)
        self.AlexCb.move(225,90)
        self.AlexCb.stateChanged.connect(partial(self.addPlayers, "Jonah" ))
        self.chkbxs.append(self.AlexCb)

        self.fourEightCb = QCheckBox('418',self)
        self.fourEightCb.move(50,130)
        self.fourEightCb.stateChanged.connect(partial(self.addGroups, "Youssef Noah Ricky" ))
        self.chkbxs.append(self.fourEightCb)

        self.dabSquad = QCheckBox('Dab Squad',self)
        self.dabSquad.move(130,130)
        self.dabSquad.stateChanged.connect(partial(self.addGroups, "Youssef Noah Ricky David" ))
        self.chkbxs.append(self.dabSquad)

    	#------------------------------------------------------------#
        self.threeButton = QPushButton('2 vs 1', self)
        self.threeButton.move(20,180)

        self.fourButton = QPushButton('2 vs 2', self)
        self.fourButton.move(170,180)

        self.threeButton.clicked.connect(self.three_click)
        self.fourButton.clicked.connect(self.four_click)
        self.show()

    def addPlayers(self, name, state):
        if state == Qt.Checked:
            self.players.append(name)
        else:
            if name in self.players:
                self.players.remove(name)

    def addGroups(self, name, state):
        if state == Qt.Checked:
            for x in name.split():
                self.players.append(x)
        else:
            for x in name.split():
                if x in self.players:
                    self.players.remove(x)
    


    def setAllButtonsChecked(self):
    	items = self.chkbxs
    	for w in items:
    		w.setChecked(False)

    def hideAllButtons(self, state):
        items = self.chkbxs
        for w in items:
            if state == Qt.Checked:
                w.hide()
                self.textbox.show()
            else: 
                w.show()
                self.textbox.hide()


    def three_click(self):
    	# get Players 

        plays = self.textbox.text().split()
        if self.YousCb.isHidden():
            players = plays
        else:
            players = self.players
        if len(players) >= 3:
            team_a = "Team 1: " + call_player(players) + " and " + call_player(players)
            team_b = "Team 2: " + call_player(players)
            QMessageBox.about(self, 'Two vs One', team_a + '\n' + '\n' +  team_b)
            self.setAllButtonsChecked()
        else:
            QMessageBox.about(self, 'caution','Gotta select at least three people bud')
            self.setAllButtonsChecked()


    def four_click(self):
    	# get Players 
        plays = self.textbox.text().split()
        if self.YousCb.isHidden():
            players = plays
        else:
            players = self.players
        if len(players) >= 4:
            team_a = "Team 1: " + call_player(players) + " and " + call_player(players)
            team_b = "Team 2: " + call_player(players) + " and " + call_player(players)
            QMessageBox.about(self, 'Two vs Two', team_a + '\n' + '\n' + team_b)
            self.setAllButtonsChecked()
        else:
            QMessageBox.about(self, 'caution','Gotta select at least four people bud')
            self.setAllButtonsChecked()



      
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


