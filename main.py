#!/usr/bin/python
# encoding: utf-8
#
#  GUI/Windows version
#  Copyright 2014: Roberto Faga Jr e Dorival Piedade Neto
#
#  http://github.com/rfaga/scriptlattesgui
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import sys
from PySide import QtCore, QtGui
from scriptLattesGUI import Ui_MainWindow

import os

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.settings = QtCore.QSettings()
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.out.insertPlainText('Aguardando entrada de dados...')
        self.ui.filechooser.clicked.connect(self.choose_file)
        self.ui.runner.clicked.connect(self.run)
        
        last_file = self.settings.value('lastFile', None)
        if last_file:
            self.ui.input.setPlainText(last_file)
        
    def print_text(self):
        s = str(self.process.readAllStandardOutput())
        try:
            s = s.decode('utf8').encode('iso-8859-15')
        except:
            pass
        self.ui.out.insertPlainText( s )
        
    def print_error(self):
        msg = "<br><p style='color: red; font-weight: bold'>%s</p>" % str(self.process.readAllStandardError()).replace('\n', '<br>')
        self.ui.errors.insertHtml(msg)
    
    def clearOutputs(self):
        self.ui.out.setPlainText('');
        self.ui.errors.setPlainText('');
        self.ui.statusbar.clearMessage()
    
    def finished(self):
        self.ui.runner.setDisabled(False)
        self.ui.runner.setText('Executar')
        self.ui.statusbar.showMessage('Processo finalizado!')
    def run(self):
        self.clearOutputs()
        self.ui.runner.setDisabled(True)
        self.ui.runner.setText('Aguarde, processando...')
        self.ui.statusbar.showMessage('Aguarde, processando...')
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.print_text)
        self.process.readyReadStandardError.connect(self.print_error)
        self.process.finished.connect(self.finished)
        filepath = self.ui.input.toPlainText()
        self.process.start('./runner.py',[filepath])

    def choose_file(self):
        last_file = self.settings.value('lastFile', None)
        if last_file:
            folder = os.path.abspath(os.path.join(last_file, os.pardir))
        else:
            folder = '.'
        filename = QtGui.QFileDialog.getOpenFileName(self,
            "Open Image", folder, "Text files (*.config)")
        path = filename[0]
        self.settings.setValue('lastFile',  path)
        self.ui.input.setPlainText(path)
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
