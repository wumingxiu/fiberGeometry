#coding:utf-8
from .origin import *
from setting.orderset import SETTING
import sys
from PyQt4.QtGui import QTextDocument, QPrinter, QApplication

def writePdf(dir_):
    newbody = originHTML.format(**htmlpara)

    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_+'.pdf')
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(newbody.decode('utf-8'))
    text.print_(printer)
    # sys.exit(app.exec_())
    # sys.exit(0)

def writePdfabs(dir_):
    updates = SETTING().get('pdfpara')
    htmlpara.update(updates)
    newbody = originHTML.format(**htmlpara)
    # with open('t.html', 'wb') as f:
    #     f.write(newbody)
    #     f.close()
    printer = QPrinter()
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(dir_)
    printer.setPageSize(QPrinter.A4)
    text = QTextDocument()
    text.setHtml(newbody.decode('utf-8'))
    text.print_(printer)