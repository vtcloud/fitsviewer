"""
Simple display window to show the headers of a FITS file
"""
import sys
import os
import pprint
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
    QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QClipboard, QAction, QKeySequence
from PyQt6.QtCore import Qt

from astropy.io import fits


__date__ = '09/02/2025'
__updated__ = '20250902'
__version__ = '0.1'
__author__ = 'V. Tolls, CfA | Harvard & Smithsonian'


class TextViewer(QMainWindow):
    """A PyQt6 window for displaying scrollable text."""
    
    def __init__(self, text, title, width, height):
        super().__init__()
        self.setWindowTitle('fitsviewer')
        self.setGeometry(50, 100, width, height)

        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Text display area
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)  # Make the text area read-only
        self.text_edit.setText(text)
        layout.addWidget(self.text_edit)
        # Create a QFont object
        font = QFont("Courier New", 12) # Set font family 
        # Apply the font to the QTextEdit
        self.text_edit.setFont(font)
        
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
        
        file_menu.addAction(copy_action)
        
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

def fitsviewer(args=None):
    """Parses command-line arguments and runs the application."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Display scrollable text in a PyQt6 window.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "-t", "--title", 
        default="Text Viewer", 
        help="Set the window title."
    )
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
    parser.add_argument(
        "-f", "--file", 
        help="Read text from a specified file. Overrides -m/--message."
    )
    parser.add_argument(
        "-m", "--message", 
        default="Default display text.", 
        help="Set the default text message to display.\nIgnored if a file is provided with -f."
    )
    
    args = parser.parse_args()

    app = QApplication(sys.argv)
    
    ipath = ''
    
    # Get text from file if specified, otherwise use message
    if args.file:
        ifile = args.file
        try:
            with fits.open(os.path.join(ipath, ifile)) as hdul:
                # hdul.info()
                hdr0 = hdul[0].header
                hdr1 = hdul[1].header
            
                text_content = pprint.pformat(hdr0)
        except FileNotFoundError:
            QMessageBox.critical(None, "Error", f"File not found: {args.file}")
            sys.exit(1)
    else:
        text_content = args.message
        
    window = TextViewer(
        text=text_content, 
        title=args.title, 
        width=args.width, 
        height=args.height
    )
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    fitsviewer()
