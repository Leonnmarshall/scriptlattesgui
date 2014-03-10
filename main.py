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
import re
import string

if 'win' in sys.platform.lower():
    os.environ['PATH'] += ";" + os.path.abspath(os.curdir + '\\Graphviz2.36\\bin')

class RunnerStream:
    def __init__(self, output):
        self.output = output
    def write(self, text):
        self.output.emit(text)
         
class RunnerThread(QtCore.QThread):
    output = QtCore.Signal(str)
    error = QtCore.Signal(str)
    def __init__(self, filename):
        super(RunnerThread,self).__init__()
        self.filename = filename
    
    def run(self):
        import runner
        output = RunnerStream(self.output)
        error = RunnerStream(self.error)
        sys.stdout = output
        sys.stderr = error
        print "Iniciando processamento (isso pode levar alguns minutos)"
        runner.run(self.filename)

class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.settings = QtCore.QSettings()
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)
        self.print_text('Aguardando entrada de dados...')
        self.ui.filechooser.clicked.connect(self.choose_file)
        self.ui.runner.clicked.connect(self.run)
        self.ui.openLink.clicked.connect(self.open_link)
        self.ui.openFolder.clicked.connect(self.open_folder)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        last_file = self.settings.value('lastFile', None)
        if last_file:
            self.ui.input.setPlainText(last_file)

        #self.output_folder = '/tmp/teste-01/'
        #self.output_folder = u'C:\\a paça\\exemplo\\teste-01\\'
        #self.ui.resultsWidget.setDisabled(False)

    def print_text(self, s):
        try:
            s = s.encode('iso-8859-1').decode('utf8')
        except:
            try:
                s = s.encode('iso-8859-1')
            except:
                pass
        try:
            self.ui.out.insertPlainText( s )
        except:
            print_error("(String não capturada)")

    def print_error(self, s):
        msg = "<br><p style='color: red; font-weight: bold'>%s</p>" % s.replace('\n', '<br>')
        self.ui.errors.insertHtml(msg)

    def clearOutputs(self):
        self.ui.out.setPlainText('');
        self.ui.errors.setPlainText('');
        self.ui.statusbar.clearMessage()
    
    def get_output_folder(self):
        if 'win' in sys.platform.lower():
            return 'file:///' + self.output_folder.replace('\\', '/')
        else:
            return 'file://' + self.output_folder
    
    def open_link(self):
        path = self.get_output_folder() +  'index.html'
        print path
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(path, QtCore.QUrl.TolerantMode))
    
    def open_folder(self):
        path = self.get_output_folder()
        QtGui.QDesktopServices.openUrl(path)
    
    def run(self):
        self.clearOutputs()
        self.ui.resultsWidget.setDisabled(True)
        
        self.current_file = self.ui.input.toPlainText()
        
        self.ui.runner.setDisabled(True)
        self.ui.runner.setText('Aguarde, processando...')
        self.ui.statusbar.showMessage('Aguarde, processando...')
        self.thread = RunnerThread(self.current_file)
        self.thread.finished.connect(self.finished)
        self.thread.output.connect(self.print_text)
        self.thread.error.connect(self.print_error)
        self.thread.start()

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


    def finished(self):
        self.ui.runner.setDisabled(False)
        self.ui.runner.setText('Executar')
        self.ui.statusbar.showMessage('Processo finalizado!')
        
        s = self.ui.out.toPlainText()
        # getting from output result folder
        results = re.findall(r"\>\'.*?\'\<", s)
        if results:
            self.output_folder = unicode(results[0][2:-2] + os.sep)
            self.ui.resultsWidget.setDisabled(False)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
