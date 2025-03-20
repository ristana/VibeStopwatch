from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QHBoxLayout
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from .styles import BUTTON_STYLE, TIME_DISPLAY_STYLE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VibeStopwatch")
        self.setMinimumSize(400, 200)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Create time display
        self.time_label = QLabel("00:00:00.000")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setFont(QFont("Arial", 48))
        self.time_label.setStyleSheet(TIME_DISPLAY_STYLE)
        layout.addWidget(self.time_label)
        
        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        # Create control buttons
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")
        
        # Apply styles to buttons
        for button in [self.start_button, self.stop_button, self.reset_button]:
            button.setStyleSheet(BUTTON_STYLE)
        
        # Add buttons to layout
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)
        
        layout.addLayout(button_layout)
        
        # Initialize timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.elapsed_time = 0
        self.is_running = False
        
        # Connect buttons to functions
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        
        # Initialize state
        self.stop_button.setEnabled(False)
        
    def start(self):
        if not self.is_running:
            self.timer.start(1)  # Update every millisecond
            self.is_running = True
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
    
    def stop(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
    
    def reset(self):
        self.stop()
        self.elapsed_time = 0
        self.update_display()
    
    def update_time(self):
        self.elapsed_time += 1  # 1 millisecond
        self.update_display()
    
    def update_display(self):
        # Convert milliseconds to hours, minutes, seconds, and milliseconds
        hours = self.elapsed_time // 3600000
        minutes = (self.elapsed_time % 3600000) // 60000
        seconds = (self.elapsed_time % 60000) // 1000
        milliseconds = self.elapsed_time % 1000
        
        # Format the time string
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        self.time_label.setText(time_str) 