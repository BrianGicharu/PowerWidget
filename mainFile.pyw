import sys

from pydub import AudioSegment
from pydub.playback import play

from os import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def cancel():
    cancel_s = AudioSegment.from_wav("cancel.wav")
    play(cancel_s)
    # system("shutdown /a")


def log_out():
    system("shutdown /l")


def shutdown():
    # This Popen reference failed
    """subprocess.Popen("vlc", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE).communicate(input=b"vlc cancel.mp3")"""
    system("shutdown /s /t 0")


def restart():
    # This Popen reference failed
    """subprocess.Popen("C:\\Windows\\System32\\cmd.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE).communicate(input=b"shutdown /r -t 0")"""
    system("shutdown /r")


def hibernate():
    # This Popen reference failed
    """subprocess.Popen("C:\\Windows\\System32\\cmd.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE).communicate(input=b"shutdown /h")"""
    system("shutdown /h")


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Windows Power Off Options")
        self.setWindowIcon(QIcon(QPixmap("icons\\icon.png")))
        self.setFixedSize(200, 180)

        layout = QGridLayout()
        self.setLayout(layout)

        # self.setStyleSheet("background-image: url(back.jpg);background-repeat: no-repeat;background-position:
        # center;")

        self.setStyleSheet("background-color:pink;background-repeat: no-repeat;background-position: center;")

        font_one = QFont()
        font_one.setFamily("Arial Rounded MT Bold")
        font_one.setPointSize(10)

        font_stress = QFont()
        font_stress.setFamily("Sans Serif")
        font_stress.setPointSize(11)
        font_stress.setBold(True)

        abt_font = QFont()
        abt_font.setFamily("Arial Black")
        abt_font.setItalic(True)
        abt_font.setPointSize(8)

        self.btn_logout = QPushButton("LOGOUT!")
        self.btn_logout.setFont(font_one)
        self.btn_logout.setIcon(QIcon(QPixmap("icons\\logout.png")))
        self.btn_logout.clicked.connect(log_out)
        self.btn_logout.setToolTip("Logs out from the current user account")
        layout.addWidget(self.btn_logout)

        self.btn_shutdown = QPushButton("SHUTDOWN!")
        self.btn_shutdown.setFont(font_one)
        self.btn_shutdown.setIcon(QIcon(QPixmap("power_off.png")))
        self.btn_shutdown.clicked.connect(shutdown)
        self.btn_shutdown.setToolTip("Shut down the Computer")
        layout.addWidget(self.btn_shutdown)

        self.btn_restart = QPushButton("RESTART!")
        self.btn_restart.setFont(font_one)
        self.btn_restart.setIcon(QIcon(QPixmap("icons\\restart.png")))
        self.btn_restart.clicked.connect(restart)
        self.btn_restart.setToolTip("Restart your computer")
        layout.addWidget(self.btn_restart)

        self.btn_hibernate = QPushButton("HIBERNATE!")
        self.btn_hibernate.setFont(font_one)
        self.btn_hibernate.setIcon(QIcon(QPixmap("icons\\hibernate.png")))
        self.btn_hibernate.clicked.connect(hibernate)
        self.btn_hibernate.setToolTip("Save the machine state, shutdown and resume with the same apps once powered on")
        layout.addWidget(self.btn_hibernate)

        self.btn_cancel = QPushButton("\tCANCEL!")
        self.btn_cancel.setFont(font_stress)
        self.btn_cancel.setIcon(QIcon(QPixmap("icons\\cancel.png")))
        self.btn_cancel.clicked.connect(cancel)
        self.btn_cancel.setToolTip("Cancel any scheduled power action")
        layout.addWidget(self.btn_cancel)

        abt_lbl = QLabel()
        abt_lbl.setText("Plancks Code Lab Creation")
        abt_lbl.setFont(abt_font)
        layout.addWidget(abt_lbl)


stylesheet = """
    Window {
        background-image: url("C:\\Users\\Brian\\IdeaProjects\\PowerWidget\\back.jpg");
        background-repeat: no-repeat;
        background-position: center;
    }
"""


def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
