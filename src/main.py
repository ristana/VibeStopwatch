#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication
from gui.window import MainWindow
from gui.styles import apply_dark_theme

def main():
    """Launch the VibeStopwatch application."""
    app = QApplication(sys.argv)
    apply_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 