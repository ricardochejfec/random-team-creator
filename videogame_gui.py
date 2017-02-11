#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import fileinput
from functools import partial
from PyQt5.QtWidgets import (qApp, QWidget,QMainWindow, QAction, QPushButton, QLineEdit, QApplication,QInputDialog, QGroupBox, QMessageBox, QCheckBox)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

def call_player(players):
    	rand_int = random.randint(0,len(players) - 1)
    	return players.pop(rand_int)

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        self.setGeometry(300,300,305,250)
        self.setWindowTitle('Videogame Teams')
        self.setWindowIcon(QtGui.QIcon('chip_icon_normal.png'))
    	# UnComment to use a textbox instead of checkboxes. 
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 80)
        self.textbox.resize(240,20)
        self.textbox.setText("Who's Playing?")
        self.textbox.hide()
    	

        #get list of permanent players
        
        self.perm_players = []
        self.perm_groups = {}
        with open('teams.txt') as f:
            content = f.readlines()
        for line in content:
            print(line[0])
            if line[0] == '#':
                self.perm_players.append(line[1:].strip())
            elif line[0] == '$':
                print(line.split('-')[0], line.split('-')[1])
                self.perm_groups[line.split('-')[0][1:]] = line.split('-')[1]
                
        
        self.players = []
        self.chkbxs = []
        
        self.modCb = QCheckBox('Custom', self)
        self.modCb.move(0,30)
        self.modCb.stateChanged.connect(self.hideAllButtons)

        #------------------------------------------------------------#

        self.YousCb = QCheckBox(self.perm_players[0], self)
        self.YousCb.move(0,70)
        self.YousCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[0] ))
        self.chkbxs.append(self.YousCb)

        self.NoahCb = QCheckBox(self.perm_players[1],self)
        self.NoahCb.move(75,70)
        self.NoahCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[1] ))
        self.chkbxs.append(self.NoahCb)

        self.RickyCb = QCheckBox(self.perm_players[2], self)
        self.RickyCb.move(150, 70)
        self.RickyCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[2] ))
        self.chkbxs.append(self.RickyCb)

        self.DavidCb = QCheckBox(self.perm_players[3],self)
        self.DavidCb.move(225,70)
        self.DavidCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[3] ))
        self.chkbxs.append(self.DavidCb)

        self.DrassCb = QCheckBox(self.perm_players[4], self)
        self.DrassCb.move(0,110)
        self.DrassCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[4] ))
        self.chkbxs.append(self.DrassCb)

        self.LucaCb = QCheckBox(self.perm_players[5],self)
        self.LucaCb.move(75,110)
        self.LucaCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[5] ))
        self.chkbxs.append(self.LucaCb)

        self.SantiCb = QCheckBox(self.perm_players[6],self)
        self.SantiCb.move(150,110)
        self.SantiCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[6] ))
        self.chkbxs.append(self.SantiCb)

        self.AlexCb = QCheckBox(self.perm_players[7],self)
        self.AlexCb.move(225,110)
        self.AlexCb.stateChanged.connect(partial(self.addPlayers, self.perm_players[7]))
        self.chkbxs.append(self.AlexCb)

        keys = sorted(self.perm_groups.keys())
        group_one = keys[0]
        self.fourEightCb = QCheckBox(group_one,self)
        self.fourEightCb.move(50,150)
        self.fourEightCb.stateChanged.connect(partial(self.addGroups, self.perm_groups[group_one]))
        self.chkbxs.append(self.fourEightCb)

        group_two = keys[1]
        self.dabSquad = QCheckBox(group_two,self)
        self.dabSquad.move(130,150)
        self.dabSquad.stateChanged.connect(partial(self.addGroups, self.perm_groups[group_two]))
        self.chkbxs.append(self.dabSquad)

    	#------------------------------------------------------------#

        self.threeButton = QPushButton('2 vs 1', self)
        self.threeButton.move(20,200)

        self.fourButton = QPushButton('2 vs 2', self)
        self.fourButton.move(170,200)

        #------------------------------------------------------------#
       
        ########### CHANGE PERMANENT PLAYERS SCREEN ATTEMP ###########
        ##############################################################
        
        self.changeButtons = []

        self.YousBtn = QPushButton(self.perm_players[0], self)
        self.YousBtn.resize(80,40)
        self.YousBtn.move(0,70)
        self.YousBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[0] ))
        self.changeButtons.append(self.YousBtn)
        self.YousBtn.hide()

        self.NoahBtn = QPushButton(self.perm_players[1],self)
        self.NoahBtn.resize(80,40)
        self.NoahBtn.move(75,70)
        self.NoahBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[1]))
        self.changeButtons.append(self.NoahBtn)
        self.NoahBtn.hide()

        self.RickyBtn = QPushButton(self.perm_players[2], self)
        self.RickyBtn.resize(80,40)
        self.RickyBtn.move(150, 70)
        self.RickyBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[2]))
        self.changeButtons.append(self.RickyBtn)
        self.RickyBtn.hide()

        self.DavidBtn = QPushButton(self.perm_players[3],self)
        self.DavidBtn.resize(80,40)
        self.DavidBtn.move(225,70)
        self.DavidBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[3]))
        self.changeButtons.append(self.DavidBtn)
        self.DavidBtn.hide()

        self.DrassBtn = QPushButton(self.perm_players[4], self)
        self.DrassBtn.resize(80,40)
        self.DrassBtn.move(0,110)
        self.DrassBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[4]))
        self.changeButtons.append(self.DrassBtn)
        self.DrassBtn.hide()

        self.LucaBtn = QPushButton(self.perm_players[5],self)
        self.LucaBtn.resize(80,40)
        self.LucaBtn.move(75,110)
        self.LucaBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[5]))
        self.changeButtons.append(self.LucaBtn)
        self.LucaBtn.hide()

        self.SantiBtn = QPushButton(self.perm_players[6],self)
        self.SantiBtn.resize(80,40)
        self.SantiBtn.move(150,110)
        self.SantiBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[6]))
        self.changeButtons.append(self.SantiBtn)
        self.SantiBtn.hide()

        self.AlexBtn = QPushButton(self.perm_players[7],self)
        self.AlexBtn.resize(80,40)
        self.AlexBtn.move(225,110)
        self.AlexBtn.clicked.connect(partial(self.substitutePlayer, self.perm_players[7]))
        self.changeButtons.append(self.AlexBtn)
        self.AlexBtn.hide()

        self.doneBtn = QPushButton('Done', self)
        self.doneBtn.resize(80,40)
        self.doneBtn.move(210,200)
        self.doneBtn.clicked.connect(self.backToNormal)
        self.changeButtons.append(self.doneBtn)
        self.doneBtn.hide()
        
        ########### CHANGE PERMANENT PLAYERS SCREEN ATTEMP ###########
        ##############################################################

        #------------------------------------------------------------#

        ###########################
            # MENU BAR ATTEMP # 
        
        #Menubar Exit
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        #Menubar Add
        addPermAction = QAction('&Add', self)
        addPermAction.setShortcut('Ctrl+A')
        addPermAction.setStatusTip('Add a permanent player')
        addPermAction.triggered.connect(self.addPermPlayer)

        menubar = self.menuBar()

        #Always use for menu bars!!!
        menubar.setNativeMenuBar(False)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu .addAction(addPermAction)
        
            # MENU BAR ATTEMP # 
        ###########################

        #------------------------------------------------------------#


        self.threeButton.clicked.connect(self.three_click)
        self.fourButton.clicked.connect(self.four_click)
        self.show()


    def backToNormal(self):
        QMessageBox.about(self, 'Warning', 'To see your changes, restart the program.')
        other_items = self.changeButtons
        for w in other_items:
            w.hide()
        items = self.chkbxs
        self.threeButton.show()
        self.fourButton.show()
        #show checkbuttons
        for w in items:
            w.show()

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

    def addPermPlayer(self):
        items = self.chkbxs
        #hide checkbuttons
        for w in items:
            w.hide()
        #hide custom
        self.textbox.hide()
        self.threeButton.hide()
        self.fourButton.hide()
        #show buttons
        other_items = self.changeButtons
        for w in other_items:
            w.show()

    def substitutePlayer(self, name, state):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Players Name:')
        if ok:
            self.rewrite_file(name,text)
            self.perm_players[self.perm_players.index(name)] = text
            self.chkbxs[self.perm_players.index(text)].setText = text
            
    def rewrite_file(self, name_out, name_in):
        # Read in the file
        filedata = None
        with open('teams.txt', 'r') as file :
            filedata = file.read()
        print(filedata)
        # Replace the target string
        filedata = filedata.replace('#'+name_out, '#'+name_in, 1)
        # Write the file out again
        with open('teams.txt', 'w') as file:
            file.write(filedata)
    
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


