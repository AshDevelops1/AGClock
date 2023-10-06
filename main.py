from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QWidget, QStackedWidget, QLabel
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QRect, Qt
import sys


class AGTimeZone(QWidget):
    """
    Timezone
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: green;")
        self.setFixedWidth(500)
        self.setFixedHeight(425)
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def run(self):
        """
        run()
        """
        pass


class AGAlarmClock(QWidget):
    """
    Timezone
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: pink;")
        self.setFixedWidth(500)
        self.setFixedHeight(425)
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


    def run(self):
        """
        run()
        """
        pass


class AGStopWatch(QWidget):
    """
    Timezone
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: blue;")
        self.setFixedWidth(500)
        self.setFixedHeight(425)
        
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


    def run(self):
        """
        run()
        """
        pass


class AGTimer(QWidget):
    """
    Timezone
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: orange;")
        self.setFixedWidth(500)
        self.setFixedHeight(425)
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)


    def run(self):
        """
        run()
        """
        pass


class MainWindow(QMainWindow):
    """
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AG Clock")
        self.setGeometry(500, 100, 500, 500)
        self.secondary_window = QStackedWidget()
        self.vbox_layout = QVBoxLayout()
        self.timezone_btn = QPushButton()
        self.alarm_btn = QPushButton()
        self.stopwatch_btn = QPushButton()
        self.timer_btn = QPushButton()
        self.time_zone = AGTimeZone()
        self.time_zone.show()
        self.alarm_clock = AGAlarmClock()
        self.alarm_clock.show()
        self.stop_watch = AGStopWatch()
        self.stop_watch.show()
        self.timer = AGTimer()
        self.timer.show()

        self.set_taskbar()
        

    def set_taskbar(self):
        """
        """
        self.vbox_layout.setContentsMargins(0, 0, 0, 0)
        self.vbox_layout.setSpacing(0)

        # self.secondary_window.setStyleSheet("background-color: yellow;")
        # self.secondary_window.setFixedWidth(500)
        # self.secondary_window.setFixedHeight(425)
        self.secondary_window.addWidget(self.time_zone)
        self.secondary_window.addWidget(self.alarm_clock)
        self.secondary_window.addWidget(self.stop_watch)
        self.secondary_window.addWidget(self.timer)
        self.secondary_window.setCurrentIndex(0)
        
        self.vbox_layout.addWidget(self.secondary_window)
        
        hbox_widget = QWidget()
        taskbar = QHBoxLayout()
        taskbar.setContentsMargins(0, 0, 0, 0)
        taskbar.setSpacing(0)
        
        self.timezone_btn.setFixedWidth(int(500/4))
        self.timezone_btn.setFixedHeight(75)
        self.timezone_btn.setText("TimeZone")
        self.timezone_btn.clicked.connect(lambda: self.load_windows(0))
        
        self.alarm_btn.setFixedWidth(int(500/4))
        self.alarm_btn.setFixedHeight(75)
        self.alarm_btn.setText("Alarm")
        self.alarm_btn.clicked.connect(lambda: self.load_windows(1))
        
        self.stopwatch_btn.setFixedWidth(int(500/4))
        self.stopwatch_btn.setFixedHeight(75)
        self.stopwatch_btn.setText("Stopwatch")
        self.stopwatch_btn.clicked.connect(lambda: self.load_windows(2))
        
        self.timer_btn.setFixedWidth(int(500/4))
        self.timer_btn.setFixedHeight(75)
        self.timer_btn.setText("Timer")
        self.timer_btn.clicked.connect(lambda: self.load_windows(3))

        taskbar.addWidget(self.timezone_btn)
        taskbar.addWidget(self.alarm_btn)
        taskbar.addWidget(self.stopwatch_btn)
        taskbar.addWidget(self.timer_btn)
        hbox_widget.setLayout(taskbar)
        self.vbox_layout.addWidget(hbox_widget)
        widget = QWidget()
        widget.setLayout(self.vbox_layout)
        self.setCentralWidget(widget)

    def load_windows(self, index):
        """
        L
        """
        if index == 0:
            self.secondary_window.setCurrentIndex(0)
            print("time_zone")
            
        elif index == 1:
            self.secondary_window.setCurrentIndex(1)
            print("alarm")
           
        elif index == 2:
            self.secondary_window.setCurrentIndex(2)
            print("stop watch")
            
        elif index == 3:
            self.secondary_window.setCurrentIndex(3)
            print("timer")
        



app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

app.exec()
