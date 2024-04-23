"""Contiene un controllo che può visualizzare i log in tempo reale."""

from PySide6 import QtWidgets
from PySide6 import QtGui


class LogWidget(QtWidgets.QFrame):
    def __init__(self, logger):
        super().__init__()
        
        self.__layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.__layout)
        
        self.__label = QtWidgets.QLabel("Log:")
        self.__layout.addWidget(self.__label)
        
        self.__text_indicator = QtWidgets.QTextEdit()
        self.__text_indicator.setMaximumBlockCount(50)
        self.__layout.addWidget(self.__text_indicator)
        
        logger.handler_function = self.__log_entry
        
    
    def __log_entry(self, entry, bb, color):
        """ """
        
        print(color)
        formato = QtGui.QTextCharFormat()
        pennello = QtGui.QBrush(color)
        formato.setForeground(pennello)

        cursor = self.__text_indicator.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(entry, formato)
        
        self.__text_indicator.moveCursor(QtGui.QTextCursor.End)        
