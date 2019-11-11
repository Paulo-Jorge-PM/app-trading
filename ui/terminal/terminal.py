#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

class Console(object):
    def __init__(self):
        tree = self.directoryTree()
        message = u"Aplicação (Python) iniciada com sucesso\nMódulo atual: UI.Terminal()\nEm construção...\n\n"
        self.printConsole(tree + "\n\n" + message)
              
    def directoryTree(self):
        tree = u"ESTRUTURA DO DIRECTÓRIO ATUAL:\n"
        for path, dirs, files in os.walk("."):
            if files != "__init__.py":
                tree += path + "\n"
            for f in files:
                if f not in ["__init__.py", "__init__.pyc"]:
                    tree += "\t" + f + "\n"
        return(tree)
        
    def printConsole(self, message):
        print(message)
        raw_input(u"Pressione enter para encerrar:")
