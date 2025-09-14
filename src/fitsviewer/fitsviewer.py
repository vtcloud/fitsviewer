"""
Simple display window to show the headers of a FITS file
"""
import sys
import os
import pprint
import io
from contextlib import redirect_stdout
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
    QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy,
    QFileDialog)
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QClipboard, QAction, QKeySequence
from PyQt6.QtCore import Qt

from astropy.io import fits
import argparse
import textwrap


__date__ = '09/02/2025'
__updated__ = '20250902'
__version__ = '0.1'
__author__ = 'V. Tolls, CfA | Harvard & Smithsonian'

path = './'

class TextViewer(QMainWindow):
    """A PyQt6 window for displaying scrollable text."""
    
    def __init__(self, text, title, width, height):
        super().__init__()
        self.setWindowTitle('fitsviewer')
        self.setGeometry(50, 100, width, height)

        # Main widget and layout
        central_widget = QWidget()
        bottom_widget = QPushButton(text="Quit")
        
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # horizontal layout for the bottom part
        bottom_layout = QHBoxLayout()
        # Add a stretchable space to push the button to the right
        bottom_layout.addStretch(1) 


        # Text display area
        self.text_edit = QTextEdit()
        self.text_edit.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding
        )
        self.text_edit.setReadOnly(True)  # Make the text area read-only
        self.text_edit.setText(text)
        main_layout.addWidget(self.text_edit)
        
        # Create a QFont object
        font = QFont("Courier New", 12) # Set font family 
        self.text_edit.setFont(font)
        
        # Add a quit button 
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(QApplication.instance().quit)
        bottom_layout.addWidget(self.quit_button)
        
        main_layout.addLayout(bottom_layout)
        
        # Add a "Copy All" menu action
        self._setup_menu()

    def _setup_menu(self):
        """Creates a menu with a 'Copy All' action."""
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        
        copy_action = QAction("Copy All", self)
        copy_action.setShortcut(QKeySequence("Cmd+A"))
        copy_action.setStatusTip("Copy all text to the clipboard")
        copy_action.triggered.connect(self.copy_all_text)

        load_action = QAction("Load File", self)
        load_action.setShortcut(QKeySequence("Cmd+F"))
        load_action.setStatusTip("Load a File")
        load_action.triggered.connect(self.load_file)
        
        file_menu.addAction(copy_action)
        file_menu.addAction(load_action)
        
        # Add a close action
        close_action = QAction("Close", self)
        close_action.setShortcut(QKeySequence("Cmd+Q"))
        close_action.setStatusTip("Close the window")
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

    def copy_all_text(self):
        """Copies all text from the QTextEdit to the system clipboard."""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_edit.toPlainText())
        
        # Show a confirmation message
        QMessageBox.information(self, "Copied", "All text has been copied to the clipboard.")

    def load_file(self):
        # to be added
        ifile = QFileDialog.getOpenFileName(self,
                "Select FITS File", path, "FITS-Files (*.fits *.fit)")
        hdr_text = load_headers(ifile[0])
        self.text_edit.setText(hdr_text)

        

def fitsviewer():
    """Parses command-line arguments and runs the application."""
    import argparse
    
    tpipe = 'fitsviewer'
    
    parser = argparse.ArgumentParser(
        prog=tpipe,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            fitviewer
            -----------------------
                I have indented it
                exactly the way
                I want it
            '''))

    parser.add_argument('filename',
        nargs='?',
        default=None,
        type=str,
    )

    parser.add_argument('-f', '--File', nargs='?', type=str,
                        help=f'{tpipe} input file.')
    
    parser.add_argument(
        "-w", "--width", 
        type=int, 
        default=800, 
        help="Set the window width in pixels."
    )
    
    parser.add_argument(
        "-H", "--height", 
        type=int, 
        default=600, 
        help="Set the window height in pixels."
    )
    args = parser.parse_args()

    app = QApplication(sys.argv)
    
    ipath = ''
    
    global path
    # Get text from file if specified, otherwise use message
    if args.filename:
        print('fitsviewer: Loading file: ', args.filename, flush=True)
        
        ifile = args.filename
        head, tail = os.path.split(ifile)
        path = head

        hdr_text = load_headers(ifile)
    elif args.File:
        #global path
        print('fitsviewer: Loading file: ', args.File, flush=True)
        
        ifile = args.File
        head, tail = os.path.split(ifile)
        path = head

        hdr_text = load_headers(ifile)
    else:
        text_content = 'Please execute with: fv -f <path-to-fits-file>'
        hdr_text = 'No file loaded!'
        
    window = TextViewer(
        text=hdr_text, 
        title='fitsviewer', 
        width=args.width, 
        height=args.height
    )
    window.show()
    
    sys.exit(app.exec())

def load_headers(ifile):
    try:
        hdr_text = ''
        with fits.open(ifile) as hdul:
            # hdul.info()
            f = io.StringIO()
            with redirect_stdout(f):
                hdul.info()
            hdul_info = f.getvalue()
            n_hdr = len(hdul)
            hdr_text = 'File: %s\n\n'%(ifile) + hdul_info + '\n\n'
            
            for i in range(n_hdr):
                hdr = hdul[i].header
                
            
                hdr_text += 'Header %i:\n\n'%(i)
                hdr_text += pprint.pformat(hdr)
                hdr_text += '\n\n##################################################\n\n'
        return hdr_text
    except FileNotFoundError:
        QMessageBox.critical(None, "Error", f"File not found: {ifile}")
        sys.exit(1)


# if __name__ == "__main__":
#     fitsviewer()
